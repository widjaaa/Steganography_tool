import sys
import struct
import numpy
import matplotlib.pyplot as plt
from PIL import Image

#mengubah data binary menjadi array bit
def decompose(data):
    v = []
    #simpan panjang file dalam 4 byte pertama (little endian)
    f_size = len(data)
    size_bytes = struct.pack("<i", f_size)

    #gabungkan header ukuran dengan data asli
    all_bytes = size_bytes + data

    for b in all_bytes:
        for i in range(7, -1, -1):
            v.append((b >> i) & 1)
    return v

#menyusun kembali array bit menjadi data biner
def assemble(v):
    byte_list = bytearray()
    length = len(v)

    for idx in range(0, length // 8):
        byte = 0
        for i in range(0, 8):
            byte = (byte << 1) + v[idx * 8 + i]
        byte_list.append(byte)
    
    #ambil 4 byte pertama untuk mengetahui panjang asli payload
    payload_size = struct.unpack("<i", byte_list[:4])[0]
    return byte_list[4 : payload_size + 4]
#mengubah bit ke-i dari n menjadi x
def set_bit(n, i, x):
    mask = 1 << i
    n &= ~mask
    if x:
        n |= mask
    return n

#menyisipkan payload kedalam lsb gambar
def embed(img_file, payload_path, output_name=None):
    img = Image.open(img_file)
    (width, height) = img.size
    #pastikan menggunakan RGBA agar konsisten
    img = img.convert("RGBA")
    pixels = img.load()

    print(f"[*] Input image size: {width}x{height} pixels.")
    max_size = (width * height * 3) // 8 // 1024
    print(f"[*] Usable payload size: {max_size:.2f} KB.")

    with open(payload_path, "rb") as f:
        data = f.read()
    print(f"[+] Payload size: {len(data)/1024.0:.3f} KB")
    v = decompose(data)

    # Tambahkan padding agar jumlah bit habis dibagi 3 (untuk R, G, B)
    while(len(v) % 3):
        v.append(0)
    if (len(v) / 8 / 1024.0 > max_size):
        print("[-] Cannot embed. File too large")
        sys.exit()
        
    idx = 0
    for h in range(height):
        for w in range(width):
            if idx < len(v):
                r, g, b, a = pixels[w, h]
                r = set_bit(r, 0, v[idx])
                g = set_bit(g, 0, v[idx+1])
                b = set_bit(b, 0, v[idx+2])
                pixels[w, h] = (r, g, b, a)
                idx += 3
            else:
                break
    
    output_path = output_name if output_name else img_file + "-stego.png"
    img.save(output_path, "PNG")
    print(f"[+] {payload_path} embedded successfully into {output_path}!")
    # Mengekstrak data dari LSB gambar
def extract(in_file, out_file):
    img = Image.open(in_file)
    pixels = img.load()
    (width, height) = img.size
    print(f"[+] Image size: {width}x{height} pixels.")

    v = []
    for h in range(height):
        for w in range(width):
            r, g, b, a = pixels[w, h]
            v.append(r & 1)
            v.append(g & 1)
            v.append(b & 1)
            
    data_out = assemble(v)

    with open(out_file, "wb") as f:
        f.write(data_out)
    
    print(f"[+] Written extracted data to {out_file}.")
    # Analisis statistik LSB
def analyse(in_file):
    BS = 100  # Ukuran blok
    img = Image.open(in_file).convert("RGBA")
    pixels = img.load()
    (width, height) = img.size
    
    vr, vg, vb = [], [], []
    for h in range(height):
        for w in range(width):
            r, g, b, a = pixels[w, h]
            vr.append(r & 1)
            vg.append(g & 1)
            vb.append(b & 1)

    avgB = [numpy.mean(vb[i:i + BS]) for i in range(0, len(vb), BS)]

    plt.figure(figsize=(10, 4))
    plt.plot(range(len(avgB)), avgB, 'bo', markersize=1)
    plt.title("LSB Statistical Analysis (Blue Channel)")
    plt.ylabel('Average LSB per block')
    plt.xlabel('Block number')
    plt.axis([0, len(avgB), 0, 1])
    plt.show()

def usage(progName):
    print("LSB Steganography Tool (Python 3)\n")
    print("Usage:")
    print(f"  {progName} hide <img_file> <payload_file>")
    print(f"  {progName} extract <stego_file> <out_file>")
    print(f"  {progName} analyse <stego_file>")
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage(sys.argv[0])
        
    command = sys.argv[1]
    if command == "hide" and len(sys.argv) == 4:
        embed(sys.argv[2], sys.argv[3])
    elif command == "extract" and len(sys.argv) == 4:
        extract(sys.argv[2], sys.argv[3])
    elif command == "analyse":
        analyse(sys.argv[2])
    else:
        usage(sys.argv[0])
