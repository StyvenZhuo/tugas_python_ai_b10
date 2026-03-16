# Styven - Program AI - Tugas 3


# String
about = "Styven adalah seorang siswa yang belajar di Infinite Learning khususnya dalam Program AI"
print(about)

# Integer
day = 13
month = 3
year = 2005
umur = 2026 - year
print("Styven lahir pada tanggal", day, "bulan", month, "tahun", year, "dan saat ini berumur", umur, "tahun.")

# Float
panjang = 12.5
lebar = 7.2
tinggi = 5.0
volume = panjang * lebar * tinggi 
print("Volume balok dengan panjang", panjang, "lebar", lebar,"dan tinggi", tinggi, "adalah", volume)

# Boolean
is_student = True
is_employed = False
print("Apakah Styven adalah seorang siswa?", is_student)
print("Apakah Styven bekerja?", is_employed)

# List
hobbies = ["playing basketball", "coding", "swimming"]
print("Hobi Styven adalah", hobbies[1])
print("Hobi Styven adalah", hobbies[0])

# 2. Manipulasi string
nama_awal = "Styven"
nama_akhir = "Zhuo"
nama_lengkap = nama_awal + " " + nama_akhir
print("Nama Lengkap Saya adalah", nama_lengkap)

panjang_nama = len(nama_lengkap)
print("Panjang nama lengkap saya adalah", panjang_nama, "huruf.")

# Upper and Lower Case
print("Huruf Besar", nama_lengkap.upper())
print("Huruf Kecil", nama_lengkap.lower())

# 3. Operasi Matematika
x = 100
y = 5

print("Penjumlahan:", x + y)
print("Pengurangan:", x - y)
print("Perkalian:", x * y)
print("Pembagian:", x / y)
print("Sisa Pembagian:", x % y)
print("Pembagian Bulat:", x // y)

# 4. List dan Akses Elemen
buah = ["apel", "jeruk", "pisang", "mangga", "anggur", "semangka", "kiwi", "nanas", "stroberi", "melon"]
print("Buah pertama dalam daftar belanja saya adalah", buah[0])
print("Buah terakhir dalam daftar belanja saya adalah", buah[-1])
print("Buah ke 5 dalam daftar belanja saya adalah", buah[4])

buah.append("pepaya")
print("Daftar belanja saya", buah)

buah.remove("anggur")
print("Daftar belanja saya", buah)

buah.pop(2)
print("Daftar belanja saya", buah)

# Penggunaan Input dari User
nama_user = input("Masukkan nama anda : ")
umur_user = int(input("Masukkan umur anda : "))

print(f"Halo {nama_user}, kamu termasuk ke dalam target user Snapnap karena umur kamu adalah {umur_user}")