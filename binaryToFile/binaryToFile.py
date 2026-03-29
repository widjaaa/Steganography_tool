import os

def parse_binary_text(data: bytes) -> str:
    """Mengonversi raw bytes yg berisi ASCII '0' (0x30) dan '1' (0x31) menjadi string biner murni."""
    return "".join(['1' if b == 0x31 else '0' for b in data if b in [0x30, 0x31]])

def binary_str_to_bytes(binary_str: str) -> bytearray:
    """Mengelompokkan string biner menjadi urutan raw bytes utuh (8 bit = 1 byte)."""
    byte_data = bytearray()
    for i in range(0, len(binary_str), 8):
        byte_chunk = binary_str[i:i+8]
        # Pastikan tidak ada chunk yg kurang dari 8 bit di akhir array
        if len(byte_chunk) == 8:
            byte_data.append(int(byte_chunk, 2))
    return byte_data

def convert_txt_to_file(input_file: str, output_file: str):
    """Membaca file teks berisi biner, mengkonversi valuenya, lalu menyimpan menjadi file aslinya."""
    if not os.path.exists(input_file):
        print(f"[-] Error: File input '{input_file}' tidak ditemukan dalam tempat Anda menjalankan perintah ini.")
        return

    print(f"[*] Sedang memproses file '{input_file}'...")
    try:
        # Membaca data binary text awal
        with open(input_file, 'rb') as f:
            data = f.read()
        
        # Eksekusi langkah-langkah de-coding
        binary_str = parse_binary_text(data)
        byte_data = binary_str_to_bytes(binary_str)
        
        # Simpan menjadi sebuah file hasil yang diharapkan
        with open(output_file, 'wb') as f:
            f.write(byte_data)
        
        print(f"[+] Eksekusi selesai! Berhasil menyimpan data gambar yang terekstrak ke file '{output_file}'.")
    
    except Exception as e:
        print(f"[-] Waduh, tidak disangka terjadi error selama pemrosesan: {e}")

if __name__ == "__main__":
    # Konfigurasi nama input dan output (Ubah jika diperlukan)
    INPUT_FILENAME = 'digits.bin'
    OUTPUT_FILENAME = 'hasil_flag.jpg'
    
    convert_txt_to_file(INPUT_FILENAME, OUTPUT_FILENAME)