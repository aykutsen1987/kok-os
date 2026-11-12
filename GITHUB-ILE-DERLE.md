# GitHub ile ISO derleme (kendi bilgisayarınızda Linux/disk gerekmez)
1. github.com'da ücretsiz hesap açın, "New repository" ile boş depo oluşturun (adı: kok-os).
2. "uploading an existing file" ile bu zip'in içindeki dosyaları (auto, config, README.md ...) yükleyin.
3. Depoda "Add file > Create new file" deyin, adı kısmına şunu yazın: .github/workflows/build-iso.yml
   İçine build-iso.yml dosyasının içeriğini yapıştırıp "Commit" deyin.
4. "Actions" sekmesi > "Kök OS ISO derle" > "Run workflow".
5. 40-90 dk sonra bitince, çalıştırmanın sayfasında "Artifacts" altından kok-os-iso-ve-rapor dosyasını indirin.
   İçinde ISO ve kok-build-rapor.txt var. Hata olursa raporu geliştiriciye gönderin.
