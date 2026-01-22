# 🚀 QR Master Pro: All-in-One QR Toolkit

Python ile geliştirilmiş, kullanıcı dostu bir arayüze sahip profesyonel bir QR kod yönetim aracıdır. Bu uygulama ile hem kendi QR kodlarınızı oluşturabilir hem de kamera veya dosya üzerinden anlık tarama yapabilirsiniz.

## 🌟 Öne Çıkan Özellikler

- **Hızlı QR Oluşturma:** Metin veya URL'leri saniyeler içinde `.png` formatında QR koda dönüştürür.
- **Otomatik Web Yönlendirme:** Okunan QR kod bir internet sitesi ise bilgisayarınızın tarayıcısını otomatik olarak açar.
- **Canlı Kamera Taraması:** OpenCV entegrasyonu ile kameranızı profesyonel bir barkod okuyucuya dönüştürür.
- **Resimden QR Çözme:** Bilgisayarınızdaki mevcut görselleri tarayarak içindeki veriyi ayıklar.
- **Karakter Uyumluluğu:** Türkçe karakterli dosya yollarında (Numpy desteği ile) hatasız çalışır.
  
🚀 Nasıl Kullanılır?

Proje dosyalarını indirin.

Terminali açın ve python main.py komutunu çalıştırın.

Açılan modern arayüz üzerinden:

Üst kutuya metin girip Oluştur butonuna basarak kaydedin.

Kamerayı Aç butonuna basıp QR kodunuzu kameraya gösterin.

Kamera penceresini kapatmak için klavyeden 'q' tuşuna basın.

📁 Proje Yapısı

main.py: Uygulamanın tüm mantığını ve arayüzünü içeren ana kod dosyası.

requirements.txt: Gerekli Python kütüphanelerinin listesi.

README.md: Proje dokümantasyonu.
  

## 🛠️ Teknik Gereksinimler

Projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

```bash
pip install qrcode[pil] opencv-python pyzbar numpy


