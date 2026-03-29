# Stegano LSB Tool

Tool ini digunakan untuk menerapkan teknik Steganografi menggunakan metode LSB (Least Significant Bit) pada file gambar. Tool ini memungkinkan Anda untuk menyembunyikan file rahasia ke dalam gambar, mengekstrak kembali file tersebut, dan melakukan analisis terhadap suatu gambar *stego*.

## Fitur dan Cara Penggunaan

Berikut adalah fitur yang disediakan beserta cara penggunaannya. 

> **Catatan:** Contoh perintah di bawah menjalankan script Python `stegano_lsb_tool.py`. Pastikan Anda berada di direktori yang sama dengan tempat file tersebut tersimpan.

### 1. Menyembunyikan File (Hide)
Meyembunyikan sebuah file rahasia ke dalam file gambar asli.
```bash
python3 stegano_lsb_tool.py hide [nama_gambar_asli] [nama_file_rahasia]
```

### 2. Mengekstrak File (Extract)
Membaca dan mengekstrak file rahasia yang telah disembunyikan sebelumnya di dalam gambar *stego* ke file hasil yang baru.
```bash
python3 stegano_lsb_tool.py extract [nama_file_stego] [nama_file_hasil]
```

### 3. Menganalisis Gambar (Analyse)
Menganalisis file *stego* gambar. Bermanfaat untuk melihat perubahan atau memeriksa informasi visual dari LSB gambar tersebut.
```bash
python3 stegano_lsb_tool.py analyse [nama_file_stego]
```

## Persyaratan (Requirements)
Pastikan Anda sudah menginstal *library* Python yang dibutuhkan oleh file `stegano_lsb_tool.py` sebelum menjalankannya (seperti `numpy`, `matplotlib`, atau `opencv-python` jika terdapat di dalam script).
