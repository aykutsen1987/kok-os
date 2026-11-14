# Kök OS Yol Haritası (sürüm 0.7 – ilk tam kapsam)
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
## Sonraki (gerçek cihaz testlerinden sonra)
- Gerçek eski laptop/tablet ölçümleri ve ince ayar
- ARM-only APK desteği (çeviri katmanı) değerlendirmesi
- Açılış animasyonu (Plymouth) – initramfs riski nedeniyle ayrı ve dikkatli test
- Kök'e özel APT deposu (kendi paketlerimiz olgunlaşınca)
- ISO imzalama ve v1.0 yayını
