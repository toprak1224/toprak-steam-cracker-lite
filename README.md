Toprak Steam Cracker Lite
Modern ve kullanıcı dostu bir Steam oyun yükleme aracı. Bu uygulama, Steam oyunlarını kolayca yönetmenizi ve yüklemenizi sağlar.
🚀 Özellikler

Sürükle & Bırak Desteği: ZIP dosyalarını doğrudan uygulamaya sürükleyip bırakabilirsiniz
Otomatik DLC Yönetimi: Steam API'sini kullanarak oyunun DLC'lerini otomatik olarak algılar ve yönetir
Steam Entegrasyonu: Dosyaları doğrudan Steam klasörünüze kopyalar
Otomatik Steam Yeniden Başlatma: Tek tıkla Steam'i yeniden başlatma özelliği
Sürüm Kontrolü: Yeni sürümleri otomatik olarak kontrol eder
Modern Arayüz: Siyah tema ile modern ve şık tasarım

📋 Sistem Gereksinimleri

İşletim Sistemi: Windows 10/11
Python: 3.7 veya üzeri (kaynak koddan çalıştırıyorsanız)
Steam: Bilgisayarınızda Steam kurulu olmalı

🔧 Kurulum
Hazır Executable Dosyası (Önerilen)

Releases sayfasından en son sürümü indirin
ZIP dosyasını açın
ToprakSteamCrackerLite.exe dosyasını çalıştırın

Kaynak Koddan Çalıştırma
bash# Depoyu klonlayın
git clone https://github.com/toprak1224/ToprakSteamCrackerLite.git

# Klasöre gidin
cd ToprakSteamCrackerLite

# Gerekli paketleri yükleyin
pip install -r requirements.txt

# Uygulamayı çalıştırın
python main.py
📦 Gerekli Python Paketleri
txtPySide6
requests
🎮 Kullanım
Adım 1: Steam Klasörünü Seçin

Uygulamayı açın
"Gözat" butonuna tıklayın
Steam kurulum klasörünüzü seçin (genellikle C:\Program Files (x86)\Steam)

Adım 2: Oyun Dosyasını Yükleyin

ZIP dosyasını sürükleyip bırakın veya tıklayarak seçin
Önemli: ZIP dosyasının adı oyunun Steam AppID'si olmalı (örnek: 271590.zip)

Adım 3: İşlemi Tamamlayın

Uygulama otomatik olarak:

.lua dosyalarını Steam/config/stplug-in/ klasörüne kopyalar
.manifest dosyalarını Steam/config/depotcache/ klasörüne kopyalar
DLC bilgilerini marcellus.lua dosyasına ekler


"Steam'i Yeniden Başlat" butonuna tıklayın

📁 Dosya Yapısı
Steam/
├── config/
│   ├── stplug-in/
│   │   ├── *.lua (oyun dosyaları)
│   │   └── marcellus.lua (DLC dosyası)
│   └── depotcache/
│       └── *.manifest (manifest dosyaları)
🔍 AppID Nedir?
Steam AppID, her Steam oyununun benzersiz kimlik numarasıdır. Bu numarayı şu şekilde bulabilirsiniz:

Steam Store: https://store.steampowered.com/app/271590/ - URL'deki sayı (271590)
SteamDB: steamdb.info sitesinden arama yapın
Steam Client: Oyun sayfasında URL'yi kontrol edin

⚙️ Teknik Detaylar
Desteklenen Dosya Formatları

ZIP: Oyun dosyalarını içeren arşiv
LUA: Steam plugin dosyaları
MANIFEST: Depot cache dosyaları

API Kullanımı
Uygulama, DLC bilgilerini almak için Steam Web API'sini kullanır:
https://store.steampowered.com/api/appdetails?appids={game_id}
Güvenlik

Dosyalar sadece belirlenen Steam klasörlerine kopyalanır
Zararlı dosya türleri kontrol edilir
Sürüm kontrolü güvenli HTTPS bağlantısı kullanır

🛠️ Geliştirici Bilgileri
Proje Yapısı
ToprakSteamCrackerLite/
├── main.py              # Ana uygulama dosyası
├── requirements.txt     # Python bağımlılıkları
├── favicon.png         # Uygulama ikonu
├── build.py            # Executable build scripti
└── README.md           # Bu dosya
Build Etme
bash# PyInstaller ile executable oluşturma
pip install pyinstaller
pyinstaller --onefile --windowed --icon=favicon.ico main.py
🔧 Sorun Giderme
Sık Karşılaşılan Hatalar
"Steam klasörü bulunamadı"

Steam'in doğru klasörünü seçtiğinizden emin olun
Genellikle C:\Program Files (x86)\Steam konumundadır

"ZIP dosyası AppID içermeli"

ZIP dosyasının adı sadece sayı olmalı (örnek: 271590.zip)
Dosya adında harf veya özel karakter bulunmamalı

"Steam yeniden başlatılamadı"

Uygulamayı yönetici olarak çalıştırın
Steam'in tamamen kapatıldığından emin olun

Log Dosyası
Hata ayıklama için uygulama klasöründe debug.log dosyasını kontrol edin.
📞 Destek

Discord: https://discord.gg/DnFnsM8M
GitHub Issues: Issues sayfası
E-posta: GitHub profili üzerinden iletişim kurabilirsiniz

📄 Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasını inceleyin.
🤝 Katkıda Bulunma

Bu repoyu fork edin
Yeni bir branch oluşturun (git checkout -b feature/amazing-feature)
Değişikliklerinizi commit edin (git commit -m 'Add some amazing feature')
Branch'inizi push edin (git push origin feature/amazing-feature)
Bir Pull Request açın

🌟 Özellik İstekleri
Yeni özellik önerilerinizi GitHub Issues sayfasında paylaşabilirsiniz:

 Çoklu dosya seçimi
 Tema değiştirme seçeneği
 Otomatik güncelleştirme
 Oyun bilgisi gösterimi
 İndirme geçmişi

📊 Sürüm Geçmişi
v1.0.0 (2024)

İlk sürüm
Temel sürükle & bırak özelliği
Steam entegrasyonu
DLC yönetimi
Siyah tema

⚠️ Yasal Uyarı
Bu araç yalnızca eğitim amaçlıdır. Kullanıcılar, tüm yasal sorumluluğu kendileri üstlenirler. Lütfen Steam'in Kullanım Koşullarına uygun davranın.

Made by Toprak 🚀
Bu README dosyası sürekli güncellenmektedir. Son sürüm için GitHub sayfasını kontrol edin.
