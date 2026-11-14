# Kök OS – Hata Haritası (hangi iz hangi adımdan?)

## Derleme sırasında (`kok-build-rapor.txt`)
| İşaretçi | Adım | Dosya | Anlamı |
|---|---|---|---|
| `[KOK-HATA:A2:yerellestirme]` | 2 | hooks/live/0010-* | Dil/saat dilimi ayarı başarısız |
| `[KOK-HATA:A2:servisler]` | 2 | hooks/live/0020-* | systemd servis ayarı |
| `[KOK-UYARI:A3:tema]` / `A3:tema` | 3 | hooks/live/0030-* | WhiteSur indirilemedi (Arc'a düşer) |
| `[KOK-UYARI:A4:wine]` | 4 | hooks/live/0040-* | Wine kurulamadı |
| `[KOK-UYARI:A4:waydroid]` | 4 | hooks/live/0050-* | Waydroid veya cage kurulamadı |
| `[KOK-HATA:A5:calamares]` | 5 | hooks/live/0060-* | Kurulum sihirbazı ayarı |
| `[KOK-HATA:A5:marka]` | 5 | hooks/live/0070-* | Marka/os-release/sürüm dosyası |
| `Unable to locate package X` | 2/3 | config/package-lists/*.list.chroot | Paket adı trixie'de yok |

## Çalışırken (`kok-rapor-*.txt`)
Raporun her bölümü başlıkta adımı ve ilgili dosyayı söyler: `[ADIM 2]` bellek/ZRAM/dil, `[ADIM 3]` masaüstü/tema, `[ADIM 4a]` Wine, `[ADIM 4b]` Android, `[ADIM 5]` Calamares.
Araç günlükleri: `~/.local/state/kok/<araç>.log`.

## Adım 6
| İşaretçi | Dosya | Anlamı |
|---|---|---|
| `[KOK-UYARI:A6:gorunum]` | hooks/live/0080-* | dconf/Plank ayarı uygulanamadı |
| `[KOK-UYARI:A3:tema]` | hooks/live/0030-* | WhiteSur kurulamadı (build.log'da son 25 satır yazılır) |
| rapor `[ADIM 6]` | panel, rıhtım, Kök Ayarlar günlüğü | `~/.local/state/kok/kok-ayarlar.log` |

## Adım 7
| İşaretçi | Dosya | Anlamı |
|---|---|---|
| `[KOK:A7:boot-marka]` | hooks/live/0090-*.binary | Açılış menüsü yazıları değişti (yoksa hook çalışmadı) |
| `[KOK-UYARI:A7:katalog]` | hooks/live/0100-* | Katalog JSON'u geçersiz / Python aracı derlenemedi |
| `[KOK-HATA:A7:onyukle]` | kok-android-onyukle | Önyüklü APK kurulamadı (günlük: ~/.local/state/kok/kok-android-onyukle.log) |
| rapor `[ADIM 7]` | katalog ayarı, APK klasörü, kok-uygulamalar günlüğü | |

## Adım 8
| İşaretçi / bölüm | Dosya | Anlamı |
|---|---|---|
| `[KOK-UYARI:A8:karsilama]` | hooks/live/0110-* | Araç eksik veya hazır uygulama kurulmamış |
| rapor `[SAĞLIK ÖZETİ]` | kok-saglik | Her adım için TAMAM/SORUN listesi: önce buraya bakın |
| rapor `[ADIM 8]` | kok-karsilama günlüğü, autostart | |

## Adım 9
| İşaretçi / bölüm | Dosya | Anlamı |
|---|---|---|
| `[KOK-UYARI:A9:performans]` | hooks/live/0120-* | Disk kuralı/kapanış ayarı eksik veya VirtualBox paketi kurulmamış |
| rapor `[ADIM 9]`, `[SAĞLIK ÖZETİ]` | kok-performans, kok-saglik | Boşta RAM, açılış süresi, disk zamanlayıcıları |

## Adım 10-12
| İşaretçi | Dosya | Anlamı |
|---|---|---|
| `[KOK-UYARI:A10:donanim]` | hooks/live/0130-* | Donanım paketi/araç/ayar eksik (iio-sensor-proxy, onboard, blueman, tlp ...) |
| `[KOK-UYARI:A11:guncelleme]` | hooks/live/0140-* | unattended-upgrades veya güncelleme ayarı eksik |
| `[KOK-UYARI:A12:surum]` | hooks/live/0150-* | Kılavuz / sürüm dosyası / Python aracı |
| rapor `[SAĞLIK ÖZETİ]` sonundaki **ADIM TABLOSU** | kok-saglik | Her adım için tamam/sorun sayısı: ilk buraya bakın |
| rapor `[ADIM 10]..[ADIM 12]` | xinput, iio, nmcli, rfkill, güncelleme günlükleri | |

## 0.6 ince ayar
| İşaretçi | Dosya | Anlamı |
|---|---|---|
| `[KOK-UYARI:A6:skel]` / `[KOK-UYARI:A12:son]` | hooks 0085, 0999 | Rıhtım/menü ayarları (skel-config) kopyalanamadı |
| `[KOK:A9:vbox]` `[KOK-UYARI:A9:vbox]` | hooks/live/0125-vbox | VirtualBox Guest Additions (pano) kurulumu |
| `eksik kutuphane:` | 0125-vbox | VBoxClient için eksik .so (pano çalışmaz) |
Not: GitHub web yüklemesi nokta ile başlayan klasörleri atlar. Bu yüzden kullanıcı ayarları `usr/share/kok/skel-config` içinde tutulur ve hook ile /etc/skel/.config'e kopyalanır.

## Adım 13
| İşaretçi / bölüm | Dosya | Anlamı |
|---|---|---|
| `[KOK-UYARI:A13:kimlik]` | hooks/live/0160-* | picom/en_US/sözlük/katalog/i düğmesi eksik |
| rapor `[ADIM 13]` | picom.log, kok-hakkinda.log, kok-dil.log | |
| `picom çalışıyor` SORUN | kok-profil, picom.conf | Yuvarlak köşeler çalışmıyor: Ayarlar → Görünüm'den kapatılabilir |
