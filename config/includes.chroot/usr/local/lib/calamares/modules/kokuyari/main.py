#!/usr/bin/env python3
# Kök OS: diskte değişiklik yapılmadan ÖNCE kullanıcıya açık uyarı gösterir.
#  - Yanına kur  : YEŞİL bilgi (diğer işletim sistemleri korunur)
#  - Bölümü değiştir : TURUNCU uyarı
#  - Diski sil   : KIRMIZI uyarı + onay + "SIL" yazdırma (vazgeçilirse hiçbir şey yapılmaz)
import os
import subprocess

import libcalamares


def pretty_name():
    return "Kök OS kurulum onayı"


def _zenity(argumanlar):
    """Canlı oturumun ekranında zenity penceresi açar. Dönüş: çıkış kodu, ya da pencere açılamazsa None."""
    kullanici = "kok"
    ortam = ["DISPLAY=" + os.environ.get("DISPLAY", ":0"),
             "XAUTHORITY=/home/{}/.Xauthority".format(kullanici)]
    komut = ["runuser", "-u", kullanici, "--", "env"] + ortam + ["zenity"] + argumanlar
    try:
        sonuc = subprocess.run(komut, capture_output=True, text=True)
    except Exception as hata:
        libcalamares.utils.warning("zenity calistirilamadi: {}".format(hata))
        return None, ""
    if sonuc.returncode not in (0, 1, 5):
        libcalamares.utils.warning("zenity kod {}: {}".format(sonuc.returncode, sonuc.stderr[:200]))
        return None, ""
    return sonuc.returncode, sonuc.stdout.strip()


def _secim():
    gs = libcalamares.globalstorage
    try:
        secimler = gs.value("partitionChoices")
        if isinstance(secimler, dict):
            return str(secimler.get("install", "manual"))
    except Exception:
        pass
    return "manual"


def run():
    secim = _secim()
    libcalamares.utils.debug("Kök kurulum modu: {}".format(secim))

    if secim == "erase":
        kod, _ = _zenity([
            "--question", "--width=560", "--title=Kök OS – DİKKAT: Tüm disk silinecek",
            "--ok-label=Evet, diski sil", "--cancel-label=Vazgeç (güvenli)",
            "--text=<span foreground='#d32f2f' size='x-large'><b>⚠  TÜM DİSK SİLİNECEK</b></span>\n\n"
            "Seçtiğiniz diskteki <b>bütün bölümler ve dosyalar</b> (Windows, diğer Linux sistemleri, "
            "belgeler, fotoğraflar dahil) <span foreground='#d32f2f'><b>kalıcı olarak silinecek</b></span> "
            "ve <b>geri alınamaz</b>.\n\n"
            "Diğer işletim sistemlerini korumak istiyorsanız <b>Vazgeç</b>'e basın ve "
            "kurulumda «Yanına kur» seçeneğini seçin."])
        if kod == 1 or kod == 5:
            return ("Kurulum iptal edildi", "Diski silme işlemi onaylanmadı. Diskte hiçbir değişiklik yapılmadı.")
        if kod == 0:
            kod2, yazi = _zenity([
                "--entry", "--width=480", "--title=Son onay",
                "--ok-label=Diski sil ve kur", "--cancel-label=Vazgeç",
                "--text=<span foreground='#d32f2f'><b>Son onay:</b></span> tüm veriyi silmek için "
                "aşağıya büyük harfle <b>SIL</b> yazın."])
            temiz = (yazi or "").strip().upper().replace("İ", "I")
            if kod2 != 0 or temiz != "SIL":
                return ("Kurulum iptal edildi", "Son onay verilmedi. Diskte hiçbir değişiklik yapılmadı.")

    elif secim == "replace":
        kod, _ = _zenity([
            "--question", "--width=520", "--title=Kök OS – Bölüm değiştirilecek",
            "--ok-label=Devam et", "--cancel-label=Vazgeç",
            "--text=<span foreground='#ef6c00' size='x-large'><b>⚠  Seçilen bölüm silinecek</b></span>\n\n"
            "Seçtiğiniz bölümün içindeki <b>tüm veriler silinir</b>. Diğer bölümlere dokunulmaz."])
        if kod == 1 or kod == 5:
            return ("Kurulum iptal edildi", "Bölüm değiştirme onaylanmadı. Diskte hiçbir değişiklik yapılmadı.")

    elif secim == "alongside":
        _zenity([
            "--info", "--width=520", "--timeout=15", "--title=Kök OS – Güvenli kurulum",
            "--text=<span foreground='#2e7d32' size='x-large'><b>✔  GÜVENLİ KURULUM</b></span>\n\n"
            "Windows ve diğer işletim sistemleri <b>silinmeyecek</b>. Kök OS, ayrılan boş alana kurulacak.\n"
            "Bilgisayar açılırken bir menüden işletim sistemini seçebileceksiniz.\n\n"
            "<i>Öneri: bölüm küçültmeden önce önemli dosyalarınızı yedekleyin.</i>"])

    return None
