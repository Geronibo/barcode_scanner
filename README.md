# Barcode Scanner and Product Management Application | Barkod Okuyucu ve Ürün Yönetimi Uygulaması

This project is a Python application that enables product identification, saving, and management using a barcode scanner. The application uses the OpenCV and Pyzbar libraries to read barcodes and store product information in a JSON file.

Bu proje, bir barkod tarayıcı kullanarak ürünleri tanımlamayı, kaydetmeyi ve yönetmeyi sağlayan bir Python uygulamasıdır. Uygulama, OpenCV ve Pyzbar kütüphanelerini kullanarak barkodları okur ve ürün bilgilerini bir JSON dosyasında saklar.

## Features | Özellikler
- Detecting products using a barcode scanner | Barkod tarayıcı ile ürünleri algılama
- Saving products and storing them in a JSON file | Ürünleri kaydetme ve JSON dosyasında saklama
- Viewing the product list | Ürün listesini görüntüleme
- Deleting products | Ürün silme
- Calculating the total price of scanned products | Okutulan ürünlerin toplam fiyatını hesaplama
- User-friendly interface with Tkinter | Tkinter tabanlı kullanıcı dostu arayüz

## Requirements | Gereksinimler
To run this application, the following dependencies must be installed:

Bu uygulamayı çalıştırmak için aşağıdaki bağımlılıkların kurulu olması gerekir:

```
pip install opencv-python pyzbar tkinter
```

## Usage | Kullanım

### 1. Virtual Environment (Optional) | Sanal Ortam (Opsiyonel)
To run the project in an isolated environment, you can create a virtual environment:

Projeyi izole bir ortamda çalıştırmak için bir sanal ortam oluşturabilirsiniz:
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
dvenv\Scripts\activate  # Windows
```

### 2. Running the Application | Uygulamayı Çalıştırma
To run the application:

Uygulamayı çalıştırmak için:
```sh
python app.py
```

### 3. Scanning a Barcode | Barkod Okutma
- Show the barcode to the camera when it is opened.
- Once the barcode is detected, product details will be displayed on the interface.

- Kamera açıldığında barkodu göstererek okutabilirsiniz.
- Barkod algılandığında ürün bilgileri arayüzde gösterilecektir.

### 4. Adding a Product | Ürün Ekleme
- Manually enter the **barcode, product name, and price**.
- Click the **"Add Product"** button to save the product.

- Manuel olarak bir ürün eklemek için **barkod, ürün adı ve fiyat** bilgilerini girin.
- **"Ürün Ekle"** butonuna basarak ürünü kaydedin.

### 5. Deleting a Product | Ürün Silme
- Select a product from the product list.
- Click the **"Delete Product"** button to remove it.

- Ürün listesinden bir ürünü seçin.
- **"Ürün Sil"** butonuna basarak ürünü kaldırın.

### 6. Exit | Çıkış
- Press the 'q' key on the camera display screen to exit.

- Kamera görüntüleme ekranında 'q' tuşuna basarak çıkış yapabilirsiniz.

## File Structure | Dosya Yapısı
- `app.py` → Main application code | Ana uygulama kodu
- `products.json` → File storing product information | Ürün bilgilerinin saklandığı dosya

## Important Notes | Önemli Notlar
- The application stores products in the `products.json` file while running.
- If the file does not exist, it is created automatically.

- Uygulama çalışırken ürünleri `products.json` dosyasında saklar.
- Eğer dosya yoksa, otomatik olarak oluşturulur.

## Contributing | Katkıda Bulunma
You can send a pull request or open an issue for any improvements and feedback.

Her türlü geliştirme ve geri bildirim için pull request gönderebilir veya issue açabilirsiniz.

## License | Lisans
This project is licensed under the MIT License.

Bu proje MIT Lisansı altında lisanslanmıştır.

