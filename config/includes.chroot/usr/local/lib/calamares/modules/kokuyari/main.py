#!/usr/bin/env python3
# Kök OS: diskte değişiklik yapılmadan ÖNCE kullanıcıya açık, renkli uyarı gösterir.
#  - Yanına kur      : YEŞİL bilgi (diğer işletim sistemleri korunur)
#  - Bölümü değiştir : TURUNCU uyarı
#  - Diski sil       : KIRMIZI uyarı + "SIL" yazdırma (vazgeçilirse diske hiç dokunulmaz)
import os
import subprocess

import libcalamares

KULLANICI = "kok"


def pretty_name():
    return "Kök OS kurulum onayı"


def _calistir(komut):
    ortam = ["DISPLAY=" + os.environ.get("DISPLAY", ":0"),
             "XAUTHORITY=/home/{}/.Xauthority".format(KULLANICI)]
    tam = ["runuser", "-u", KULLANICI, "--", "env"] + ortam + komut
    try:
        return subprocess.run(tam, capture_output=True, text=True).returncode
    except Exception as hata:
        libcalamares.utils.warning("pencere acilamadi: {}".format(hata))
        return None


def _diyalog(tur, baslik, metin, evet, hayir="", yaz="", sure=0):
    """Renkli pencere. Dönüş: 0 onay, 1 vazgeç, 5 süre doldu, None = pencere açılamadı."""
    komut = ["/usr/local/bin/kok-diyalog", "--tur", tur, "--baslik", baslik, "--metin", metin, "--evet", evet]
    if hayir:
        komut += ["--hayir", hayir]
    if yaz:
        komut += ["--yaz", yaz]
    if sure:
        komut += ["--sure", str(sure)]
    kod = _calistir(komut)
    if kod in (0, 1, 5):
        return kod
    libcalamares.utils.warning("kok-diyalog kod {}; zenity denenecek".format(kod))
    return None


def _zenity_onay(baslik, metin, yaz=""):
    """Yedek: sade zenity penceresi (işaretleme YOK, düz metin)."""
    kod = _calistir(["zenity", "--question", "--width=520", "--title=" + baslik, "--text=" + metin,
                     "--ok-label=Devam et", "--cancel-label=Vazgeç"])
    if kod == 0 and yaz:
        sonuc = subprocess.run(["runuser", "-u", KULLANICI, "--", "env",
                                "DISPLAY=" + os.environ.get("DISPLAY", ":0"),
                                "XAUTHORITY=/home/{}/.Xauthority".format(KULLANICI),
                                "zenity", "--entry", "--title=Son onay",
                                "--text=Tüm veriyi silmek için büyük harfle {} yazın.".format(yaz)],
                               capture_output=True, text=True)
        girilen = sonuc.stdout.strip().upper().replace("İ", "I")
        return 0 if sonuc.returncode == 0 and girilen == yaz else 1
    return kod


def _secim():
    try:
        secimler = libcalamares.globalstorage.value("partitionChoices")
        if isinstance(secimler, dict):
            return str(secimler.get("install", "manual"))
    except Exception:
        pass
    return "manual"


def run():
    secim = _secim()
    libcalamares.utils.debug("Kök kurulum modu: {}".format(secim))
    iptal = ("Kurulum iptal edildi", "Onay verilmedi. Diskte hiçbir değişiklik yapılmadı.")

    if secim == "erase":
        metin = ("Seçtiğiniz diskteki <b>bütün bölümler ve dosyalar</b> (Windows, diğer sistemler, belgeler, "
                 "fotoğraflar dahil) <span foreground='#C62828'><b>kalıcı olarak silinecek</b></span> ve geri alınamaz."
                 "\n\nDiğer işletim sistemlerini korumak istiyorsanız <b>Vazgeç</b>'e basın ve kurulumda "
                 "«Yanına kur» seçeneğini seçin.")
        kod = _diyalog("red", "TÜM DİSK SİLİNECEK", metin, "Diski sil ve kur", "Vazgeç (güvenli)", yaz="SIL")
        if kod is None:
            kod = _zenity_onay("Kök OS – DİKKAT",
                               "Seçtiğiniz diskteki BÜTÜN veriler kalıcı olarak silinecek. Emin misiniz?", yaz="SIL")
        if kod != 0:
            return iptal

    elif secim == "replace":
        metin = ("Seçtiğiniz bölümün içindeki <b>tüm veriler silinir</b>. Diğer bölümlere dokunulmaz.")
        kod = _diyalog("orange", "BÖLÜM DEĞİŞTİRİLECEK", metin, "Devam et", "Vazgeç")
        if kod is None:
            kod = _zenity_onay("Kök OS – Bölüm değiştirilecek",
                               "Seçtiğiniz bölümün içindeki tüm veriler silinecek. Devam edilsin mi?")
        if kod != 0:
            return iptal

    elif secim == "alongside":
        metin = ("Windows ve diğer işletim sistemleri <b>silinmeyecek</b>. Kök OS, ayrılan boş alana kurulacak. "
                 "Bilgisayar açılırken bir menüden işletim sistemini seçebileceksiniz."
                 "\n\n<i>Öneri: bölüm küçültmeden önce önemli dosyalarınızı yedekleyin.</i>")
        _diyalog("green", "GÜVENLİ KURULUM", metin, "Tamam, devam et", sure=20)

    return None
