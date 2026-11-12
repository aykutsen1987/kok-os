# Kök OS – live-build deposu (Adım 2 + 3 + 4 + 5)

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
