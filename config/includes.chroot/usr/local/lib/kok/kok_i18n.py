#!/usr/bin/env python3
"""Kök OS çeviri yardımcısı (Türkçe kaynak metin → İngilizce)."""
import json, os, re, sys

SOZLUK = "/usr/share/kok/ceviri-en.json"
_desenler = None


def dil():
    for k in ("LC_ALL", "LC_MESSAGES", "LANG"):
        v = os.environ.get(k, "")
        if v and v not in ("C", "POSIX"):
            return "en" if v.lower().startswith("en") else "tr"
    try:
        for satir in open("/etc/default/locale", encoding="utf-8"):
            if satir.startswith("LANG="):
                v = satir.split("=", 1)[1].strip().strip('"')
                return "en" if v.lower().startswith("en") else "tr"
    except Exception:
        pass
    return "tr"


def _yukle():
    global _desenler
    if _desenler is None:
        try:
            d = json.load(open(SOZLUK, encoding="utf-8"))
        except Exception:
            d = {}
        liste = []
        for tr, en in sorted(d.items(), key=lambda kv: len(kv[0]), reverse=True):
            on = r"(?<!\w)" if tr[0].isalnum() else ""
            son = r"(?!\w)" if tr[-1].isalnum() else ""
            liste.append((re.compile(on + re.escape(tr) + son), en))
        _desenler = liste
    return _desenler


def T(metin):
    if not isinstance(metin, str) or dil() == "tr":
        return metin
    for desen, en in _yukle():
        metin = desen.sub(lambda _m, e=en: e, metin)
    return metin


def kilavuz():
    return "/usr/share/kok/kilavuz-en.html" if dil() == "en" else "/usr/share/kok/kilavuz.html"


def agac(w):
    """Bir Gtk pencere/bileşen ağacındaki yazıları çevirir."""
    if dil() == "tr":
        return
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk

    def isle(x):
        try:
            if isinstance(x, Gtk.Window):
                t = x.get_title()
                if t:
                    x.set_title(T(t))
            if isinstance(x, Gtk.Label):
                if x.get_use_markup():
                    x.set_markup(T(x.get_label()))
                else:
                    x.set_text(T(x.get_text()))
            elif isinstance(x, Gtk.Button):
                l = x.get_label()
                if l:
                    x.set_label(T(l))
            if isinstance(x, Gtk.Notebook):
                for i in range(x.get_n_pages()):
                    tl = x.get_tab_label(x.get_nth_page(i))
                    if tl:
                        isle(tl)
            if isinstance(x, Gtk.Container):
                for c in x.get_children():
                    isle(c)
        except Exception as e:
            print("ceviri hatasi:", e, file=sys.stderr)

    isle(w)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--argv":
        for a in sys.argv[2:]:
            sys.stdout.write(T(a) + "\0")
    elif len(sys.argv) > 2 and sys.argv[1] == "--t":
        print(T(sys.argv[2]))
