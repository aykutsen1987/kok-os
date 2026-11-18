# Kök OS 0.9

Eski ve yeni bilgisayarlar için hafif, şık ve Türkçe bir Linux (Debian 13 tabanlı).
Windows programları (Wine), Android uygulamaları (Waydroid) ve Linux uygulamaları (Flatpak) tek sistemde.

## İndirme ve kurulum
1. Sağdaki **Releases** bölümünden en son sürümü açın.
2. ISO'yu (ya da `.001`, `.002` parçalarını), `SHA256SUMS.txt` ve **Kok-OS-Kurulum-Rehberi.pdf** dosyalarını indirin.
3. Rehberdeki adımları izleyin: USB'ye yazın (Rufus, DD modu), bilgisayarı USB'den başlatın, **Kök OS'u Kur**'a tıklayın.

**Gereksinim:** 64-bit işlemci, en az 2 GB RAM (4 GB önerilir), 25 GB disk. Kurulumda internet gerekmez.
Windows'un yanına kurulumda diğer sistemler korunur; "Diski sil" seçeneği ise kırmızı uyarıyla çift onay ister.

## ISO'yu kendiniz derleme
GitHub Actions ile otomatik derlenir: **Actions → Kök OS ISO derle → Run workflow**.
Derleme sonunda ISO, **Artifacts** bölümünde çıkar. Yayınlamak için `yayinla` seçeneğini `true` yapın
ya da `v0.9` gibi bir etiket (tag) gönderin; ISO, GitHub'ın 2 GB dosya sınırı nedeniyle parçalara bölünerek **Releases**'e eklenir.

## Depo yapısı
- `auto/`, `config/` : live-build ayarları, paket listeleri, kancalar ve sisteme giren dosyalar
- `.github/workflows/build-iso.yml` : otomatik derleme ve yayınlama
- `kok-build-rapor.sh` : derleme raporu (hata ayıklama için)
- `docs/` : kurulum rehberi (PDF)
