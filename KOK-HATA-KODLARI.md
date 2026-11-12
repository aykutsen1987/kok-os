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
