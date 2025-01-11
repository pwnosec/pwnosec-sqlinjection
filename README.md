# Pwnosec SQL Injection Tool

Pwnosec SQL Injection Tool adalah alat otomatisasi untuk menguji kerentanan SQL Injection pada aplikasi web. Alat ini dirancang untuk membantu peneliti keamanan dan pengembang dalam mengidentifikasi dan memahami potensi kerentanan SQL Injection di aplikasi mereka. Dengan menggunakan alat ini, pengguna dapat melakukan pengujian terhadap berbagai payload SQL Injection dan menyimpan hasilnya untuk analisis lebih lanjut.

## Fitur

- **Pengujian SQL Injection**: Menguji kerentanan SQL Injection menggunakan berbagai payload yang dapat disesuaikan.
- **Deteksi Tipe Database**: Mendeteksi jenis database yang digunakan berdasarkan respons server.
- **Pengujian Parameter Dinamis**: Mengizinkan pengguna untuk menentukan parameter mana yang ingin diuji dalam URL.
- **Pengujian Berbasis Waktu**: Menggunakan teknik SQL Injection berbasis waktu untuk menguji kerentanan.
- **Pengujian Multi-URL**: Mengizinkan pengguna untuk menguji beberapa URL sekaligus.
- **Penyimpanan Hasil**: Menyimpan hasil pengujian ke dalam file JSON untuk analisis lebih lanjut.
- **Pengaturan Timeout**: Menambahkan pengaturan timeout untuk permintaan HTTP untuk menghindari permintaan yang menggantung.

## Cara Penggunaan

1. **Cloning Repository**:
```bash
   git clone https://github.com/pwnosec/pwnosec-sqlinjection.git
   cd pwnosec-sqlinjection
```
2. Instalasi Dependensi: Pastikan Anda memiliki Python dan pip terinstal. Kemudian, instal dependensi yang diperlukan:
```
pip install requests
```
3. Menyiapkan Payloads: Buat file `payloads.txt` yang berisi payload SQL Injection, satu per baris. Contoh:
```
' OR '1'='1
' OR '1'='1' -- 
' OR '1'='1' /* 
' UNION SELECT NULL, username, password FROM users -- 
```
4. Menjalankan Alat: Edit file `main.py` untuk menentukan URL target dan parameter yang ingin diuji. Kemudian jalankan:
**Configuration URL Targets :**
```python
if __name__ == "__main__":
    target_url = "https://www.redacted.com/en/gtarget?id=0"  # Ganti dengan URL target Anda
    payload_file = "payloads.txt"  # File yang berisi payload
    output_file = "results.json"  # File untuk menyimpan hasil
```
```
python3 main.py
```
5. Melihat Hasil: Hasil pengujian akan disimpan dalam file `results.json`.

[![asciicast](https://asciinema.org/a/0npTBsLOfiRles1wGuEKzmpvt.svg)](https://asciinema.org/a/0npTBsLOfiRles1wGuEKzmpvt)
