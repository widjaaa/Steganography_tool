# Binary to File Converter (`binaryToFile.py`)

Tool sederhana menggunakan Python yang mempermudah proses de-coding atau ekstraksi data _raw binary text_ (contoh: berisi karakter ASCII `'0'` dan `'1'`) menjadi sebuah format struktur file _bytes_ utuh atau aslinya secara rekursif. 

Skrip ini sering kali sangat berguna saat melakukan fase _Post-Extraction_ pada penyelesaian *Capture The Flag* (CTF) di tahapan steganografi atau enkripsi digital foresik, di mana Anda baru saja mengekstrak deretan kode bit tersembunyi yang "berformat teks", dan bermaksud menyusun ulang _bit-chunk_ tadi (kelompok tiap 8-bit) untuk menjadikannya _byte_ demi  menemukan _Flag_ / konten gambar, audio, atau PDF yang asli.

## Fitur

- **Parse Binary Data**: Membaca serangkaian _raw binary string_ ('1' / '0' dalam hex `0x31` `0x30`) menjadi representasi array murni.
- **Bits Assembling**: Menyusun ulang rentetan bit per bagian (*chunks* 8-bit) secara otomatis di-*cast* menjadi nilai Integer kemudian Byte.
- **File Restoration**: Menulis (*write binary / wb*) *list of bytes* hasil de-coding menjadi identitas file yang final (misalnya merekonstruksi ke ekstensi `.jpg`, `.pdf`, dsb).
- **Error Handling**: Sudah dilengkapi *try-catch block* serta pesan peringatan log jika file *input* tidak berhasil ditemukan agar membantu kemudahan diagnosa Anda.

## Prasyarat (Requirements)

Tool ini murni menggunakan pustaka bawaan standar (*built-in module*) dari instalasi **Python 3.x**. 
Anda **tidak perlu** melakukan instalasi depedensi pihak ketiga/eksternal (*No `pip install` required*).

## Cara Penggunaan

1. **Siapkan File Input**:
   Pastikan Anda sudah memiliki file masukan yang akan berisi sekuens string '*binary*' Anda. (*berdasarkan code aslinya, contoh file default adalah `digits.bin`*).
   Pastikan file tersebut berada di *directory*/folder yang sama dengan file `binaryToFile.py`.

2. **Sesuaikan Variabel Target File (Bila Perlu)**:
   Periksa konfigurasi default pada blok *execution* paling bawah dalam baris kode *script*:
   ```python
   if __name__ == "__main__":
       # Konfigurasi nama input dan output (Ubah jika diperlukan)
       INPUT_FILENAME = 'digits.bin'
       OUTPUT_FILENAME = 'hasil_flag.jpg'
   ```
   **Ganti** nama-nama file pada variabel di atas jika yang ingin Anda proses saat ini bukanlah `'digits.bin'`, dan hasil rilis ekstensi file yang mau Anda ciptakan bukanlah `'hasil_flag.jpg'`.

3. **Jalankan Eksekusi Terminal**:
   Buka terminal/Command Prompt Anda, arahkan (`cd`) ke dalam folder yang menampung `binaryToFile.py`. Lalu cukup ketik:
   
   ```bash
   python binaryToFile.py
   ```
   *(Bisa juga menggunakan standar komando `python3 binaryToFile.py` bergantung dari ENV OS Sistem).*

4. **Cek Hasil**:
   Apabila tidak terjadi mal-fungsi pada data, *output* terminal akan menunjukkan log:
   `[+] Eksekusi selesai! Berhasil menyimpan data gambar yang terekstrak ke file 'nama_file_anda.jpg'.`
   Dan file siap diuji kelayakannya!
