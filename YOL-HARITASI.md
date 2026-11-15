# Kök OS Yol Haritası (sürüm 0.8)
## Tamamlanan (ilk sürüm, test aşamasında)
1. Mimari ve teknoloji yığını (Debian 13, Xfce, Wine, Waydroid)
2. Çekirdek ve temel yapılandırma (ZRAM, earlyoom, Türkçe, live-build)
3. Masaüstü (Xfce, rıhtım, tema)
4. Windows (.exe / Wine) ve Android (.apk / Waydroid) katmanları
5. Calamares Türkçe kurulum, Kök markası, hata raporu sistemi
6. Görsel cila, üst panel, rıhtım, Kök Ayarlar merkezi
7. Android uygulama kataloğu, önyüklü APK, açılış menüsü markası
8. Karşılama penceresi, Sağlık Kontrolü, hazır uygulamalar
9. Eski donanım performansı (disk zamanlayıcı, hızlı kapanış, Performans Özeti)
10. Donanım: dokunmatik, ekran döndürme, Bluetooth, Wi-Fi, pil
11. Güncelleme: Kök Güncelleme aracı, otomatik güvenlik güncellemesi
12. Kılavuz, sürüm 0.7, SHA256 sağlama toplamı
13. Kimlik ve dil: Hakkında (i) düğmesi, @aykutsen1987 bağlantıları, Türkçe/İngilizce, Android kataloğu (Play), yuvarlak köşeler, GitHub geri bildirim
14. Giriş ve yuvarlak köşe düzeltmeleri (sürüm 0.8): 'kok' kullanıcısı ISO derlenirken oluşturulur (hook 0165) ve açılışta yedek betik (kok-kullanici-hazirla) ile garanti edilir; picom güvenilir başlatıcıyla (kok-picom-baslat, 3 deneme, günlük, yedek kompozitör) açılır; yuvarlak köşe yarıçapı 14; Sağlık Kontrolü yanlış alarmları giderildi
15. Kurulum ve uyumluluk (sürüm 0.8): kurulumda iki mod — YEŞİL «Yanına kur» (Windows/diğer sistemler silinmez, varsayılan) ve KIRMIZI «Diski sil» (uyarı + «SIL» yazarak çift onay; vazgeçilirse diske dokunulmaz); açılışta GRUB menüsünde tüm işletim sistemleri (os-prober, UEFI/BIOS, Secure Boot dosyaları); kurulu sistemde canlı «kok/live» hesabı silinir; Flatpak/Flathub, AppImage, Winetricks, 7-Zip/DMG, yazıcı desteği; VirtualBox konuk araçları için 3 yöntemli çıkarma (bsdtar, 7z, xorriso)
## Sonraki (gerçek cihaz testlerinden sonra)
- Kök OS Eski (32-bit): Debian 13 artık i386 çekirdek/kurulum sağlamaz; ayrı, Debian 12 tabanlı, Waydroid'siz hafif sürüm olarak planlandı
- Android uygulama listesi: adlar ve adresler gelince katalog doldurulacak
- Kurulum modüllerinin gerçek bilgisayarda test edilmesi: BIOS, UEFI, Windows'lu disk, boş disk
- VirtualBox pano/sürükle-bırak: derleme günlüğündeki [KOK-UYARI:A9:vbox] satırlarına göre Guest Additions kurulumunun düzeltilmesi
- Kök Ayarlar'a "Yuvarlak köşeler" ve "Köşe yarıçapı" kaydırıcısı
- Kurulu sistemde (Calamares sonrası) kullanıcı/parola akışının test edilmesi
- Gerçek eski laptop/tablet ölçümleri ve ince ayar
- ARM-only APK desteği (çeviri katmanı) değerlendirmesi
- Açılış animasyonu (Plymouth) – initramfs riski nedeniyle ayrı ve dikkatli test
- Kök'e özel APT deposu (kendi paketlerimiz olgunlaşınca)
- ISO imzalama ve v1.0 yayını
