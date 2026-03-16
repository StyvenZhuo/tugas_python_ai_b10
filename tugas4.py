# Styven - Program AI - Tugas 4
# Python Data Structures

# 1. List
catatan_harian = ["Bangun tidur", 6, 7, "Pergi Kerja", 7.30, "Buka Laptop", 8.30, "Mulai Bekerja"]
print("Catatan Harian Saya :", catatan_harian)

print("Elemen terakhir dari Catatan Harian Saya", catatan_harian[-1])
print("Elemen pertama dari Catatan Harian Saya", catatan_harian[0])

print("Slicing (indeks 1 sampai 4):", catatan_harian[1:5])
print("Slicing (indeks 2 sampai akhir):", catatan_harian[2:8])
print("Slicing (indeks 0 sampai 3):", catatan_harian[0:4])

catatan_harian.append("Istirahat")
print("Catatan Harian Saya setelah menambahkan istirahat:", catatan_harian)

catatan_harian.insert(2, "Sarapan")
print("Catatan Harian Saya setelah menyisipkan sarapan:", catatan_harian)

catatan_harian.extend(["Makan Siang", "Olahraga"])
print("Catatan Harian Saya setelah menambahkan makan siang dan olahraga:", catatan_harian)

kegiatan_pop = catatan_harian.pop(2)
print(f"Setelah pop() (mengambil '{kegiatan_pop}'):", catatan_harian)

catatan_harian.remove("Pergi Kerja")
print("Catatan Harian Saya setelah menghapus 'Pergi Kerja':", catatan_harian)
print("\n")

# Tuple
my_tuple = ("Python", 3.14, "AI", 2026, "ENV", "Opus", "4.6")
print("Tuple Saya:", my_tuple)
print("Panjang Tuple Saya", len(my_tuple))
print("Akses Indeks ke-3", my_tuple[5])

python, Opus, *sisa = my_tuple
print("Nilai python:", python)
print(f"python = {python}, Opus = {Opus}")
print(f"sisa elemen = {sisa}")
print("\n")

# Set
set_A = {1, 2, 3, 4, 5, 5}
set_B = {4, 5, 6, 7, 8}

print("Set A (duplikat hilang otomatis)", set_A)
print("Set B", set_B)

print("Union (|)", set_A | set_B)
print("Intersection (&)", set_A & set_B)
print("Difference (-)", set_A - set_B)
print("Symmetric Difference (^)", set_A ^ set_B)
print("\n")

# Dictionary
mahasiswa = {
    "nama": "Styven",
    "npm": "122334567",
    "angkatan": 2023,
    "kota": "Batam"
}
print("Dictionary awal:", mahasiswa)


mahasiswa["fakultas"] = "Ilmu Komputer" 
mahasiswa["angkatan"] = 2024          
del mahasiswa["npm"]

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("Iterasi key: value")
for key, value in mahasiswa.items():
    print(f"- {key}: {value}")
print("\n")

# Nester Structure
daftar_buku = [
    {"judul": "Python Basics", "penulis": "John Doe", "tahun": 2019},
    {"judul": "AI Mastery", "penulis": "Jane Smith", "tahun": 2022},
    {"judul": "Deep Learning", "penulis": "Alan T", "tahun": 2023},
    {"judul": "Data Science", "penulis": "Marie C", "tahun": 2020}
]

print("Semua judul buku")
for buku in daftar_buku:
    print(f"- {buku['judul']}")

buku_baru = [buku["judul"] for buku in daftar_buku if buku["tahun"] >= 2022]
print("Buku terbit >= 2022:", buku_baru)
print("\n")

# Comprehension & utilitas
genap = [x for x in range(1, 21) if x % 2 == 0]
kuadrat = [x**2 for x in range(1, 21)]
print("List Genap (1-20):", genap)
print("List Kuadrat (1-20):", kuadrat)

status_angka = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print("Dict genap/ganjil:", status_angka)

kalimat = "Belajar Python itu seru bro"
huruf_unik = {huruf.lower() for huruf in kalimat if huruf != " "}
print("Huruf unik dari kalimat:", huruf_unik)
print("\n")

# Keanggotaan & pencarian sederhana
target_angka = 20
target_huruf = "p"
print(f"Apakah {target_angka} ada di list genap? {'Ya' if target_angka in genap else 'Tidak'}")
print(f"Apakah '{target_huruf}' ada di set huruf_unik? {'Ya' if target_huruf in huruf_unik else 'Tidak'}")

if target_angka in genap:
    posisi = genap.index(target_angka)
    print(f"Angka {target_angka} ditemukan pada index ke-{posisi} di dalam list genap.")