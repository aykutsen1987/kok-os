# Kök OS – live-build deposu (Adım 2-13, sürüm 0.7)

## Gereksinimler
Debian 12/13 veya Ubuntu çalışan bir bilgisayar (veya sanal makine), ~20 GB boş disk, internet.

    sudo apt install live-build git

## ISO üretme
    cd kok-os
    sudo lb clean
    sudo lb config
    sudo lb build

Süre: internet hızına göre 20-60 dk. Sonuç: live-image-amd64.hybrid.iso

## Test (sanal makine)
    qemu-system-x86_64 -enable-kvm -m 4096 -cdrom live-image-amd64.hybrid.iso

veya VirtualBox: Debian 64-bit, 4 GB RAM, 3D hızlandırma açık.

## Notlar
- Canlı oturum kullanıcısı: kok (otomatik giriş)
- Calamares kurulumu Türkçe marka ile Adım 5'te cilalanacak.
- Adım 4: .exe (Wine) ve .apk (Waydroid) desteği eklendi.
- .exe dosyasına çift tıklayın: kendi izole ortamında çalışır.
- Android: menüden 'Android Ortamını Kur' (≥4 GB RAM, ~1 GB indirme, internet gerekir).
- Canlı oturumda Android kurulumu kapatınca silinir; kalıcı kullanım için diske kurun.
- Waydroid sanal makinede (VirtualBox) çoğu zaman ÇALIŞMAZ; gerçek donanımda deneyin.
- Wine/Waydroid hook'ları hata verirse derleme durmaz, build.log'da 'UYARI' arayın.
- Rıhtım (Plank) ve panel düzeni ilk görsel testten sonra cilalanacak.

## Hata bildirimi (en önemli bölüm)
1. **Derleme hatası:** `sudo lb build` bitince (başarısız olsa da) `kok-build-rapor.txt` oluşur. İçeriğini gönderin.
   Elle üretmek için: `./kok-build-rapor.sh`
2. **ISO açıldıktan sonra sorun:** Masaüstündeki **"Hata Raporu Oluştur"** simgesine çift tıklayın.
   Ev klasörünüzde `kok-rapor-TARİH.txt` oluşur. İçeriğini gönderin.
3. Kurulum sihirbazı (Calamares) hatalarında da aynı raporu alın; kurulum günlüğü içinde.
4. İz haritası için `KOK-HATA-KODLARI.md` dosyasına bakın.

## Adım 6
Üst panel (Kök menüsü), rıhtım düzeni, duvar kâğıdı, giriş ekranı ve **Kök Ayarlar** merkezi (Uygulamalar menüsü → Kök Ayarlar).

## Adım 7: Android uygulama kataloğu
- Menü/rıhtımdaki **Android Uygulamaları** simgesi yayıncı kataloğunu gösterir.
- Kendi listeniz için `config/includes.chroot/etc/kok/android-katalog.conf` içindeki `KATALOG_URL` alanına JSON adresinizi (https) yazın.
- Gömülü liste: `config/includes.chroot/usr/share/kok/android-katalog.json`
- Önyüklü uygulama: APK'yı `config/includes.chroot/usr/share/kok/apk/` içine koyun (Android kurulumundan sonra otomatik yüklenir).

## Adım 8
- Açılışta **Kök Karşılama** penceresi, masaüstünde **Sağlık Kontrolü** simgesi.
- Hata raporu en üstte adım adım TAMAM/SORUN özeti verir.
- Hazır uygulamalar: VLC, Evince, LibreOffice Writer/Calc, Hesap Makinesi, Görev Yöneticisi.

## Adım 9
Disk zamanlayıcı kuralı, hızlı kapanış, **Performans Özeti** (Kök Ayarlar > Genel), VirtualBox pano desteği, rıhtım kopyalarının giderilmesi.

## Adım 10-12
- Kök Ayarlar → **Donanım**: ekran döndürme, ekran klavyesi, Bluetooth, Wi-Fi, güç. Panelde pil göstergesi.
- **Kök Güncelleme** + otomatik güvenlik güncellemesi. Sürüm duyurusu için `config/includes.chroot/etc/kok/guncelleme.conf` içine SURUM_URL yazın.
- **Kullanım Kılavuzu** (Karşılama ve Ayarlar'dan açılır).
- Workflow ISO'yu `kok-os-0.5-amd64.iso` adıyla ve `SHA256SUMS.txt` ile yükler.

## Tek rapor
Masaüstü **Hata Raporu Oluştur** → tüm adımlar (2-12) tek dosyada; en üstte SAĞLIK ÖZETİ ve ADIM TABLOSU.

## Adım 13
- Panelde ve masaüstünde **"i"** düğmesi: sürüm, geliştirici (@aykutsen1987 tıklanınca diyalog), YouTube ve Play Store.
- **Dil:** Kurulumda Calamares'ten, sonradan Kök Ayarlar → Dil'den Türkçe/English.
- **Android Uygulamaları:** `usr/share/kok/android-katalog.json` (ad, açıklama, Play bağlantısı, simge, öneri).
- **Yuvarlak köşeler** (picom): Standart profilde açık, Kök Ayarlar → Görünüm'den kapatılabilir.
- **GitHub:** derleme raporu Actions çalıştırma sayfasında görünür. Cihazdan göndermek için `etc/kok/geri-bildirim.conf` içine GITHUB_DEPO yazın.
