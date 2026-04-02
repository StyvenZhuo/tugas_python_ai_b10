================================================================================
                    DOKUMENTASI TUGAS PYTHON AI - BATCH 10
================================================================================

Halo! Dokumen ini berisi ringkasan dari semua tugas yang sudah dikerjakan, 
mulai dari Tugas 3 sampai Tugas 6. Setiap bagian menjelaskan apa yang dipelajari 
dan diimplementasikan.

================================================================================
TUGAS 3 - Pengenalan Python Dasar
================================================================================

Fokus utama: Memahami tipe data dasar dan operasi dasar di Python.

Yang dipelajari:
- String: Menyimpan dan memanipulasi text
- Integer: Bilangan bulat untuk perhitungan
- Float: Bilangan desimal untuk volume, panjang, dll
- Boolean: Nilai True/False untuk logika
- List: Kumpulan data (hobi, buah-buahan, dll)
- Manipulasi string: concatenation, upper(), lower(), len()
- Operasi matematika: penjumlahan, pengurangan, perkalian, pembagian, modulo
- List methods: append(), remove(), pop()
- Input dari user: Mengambil data dari keyboard

Apa yang dibikin:
Program sederhana yang menampilkan informasi pribadi seperti nama, tanggal lahir, 
umur, hobby, dan daftar belanja. Juga menghitung volume balok dan menerima input 
dari pengguna.

Contoh output:
- Informasi pribadi Styven yang tersimpan dalam berbagai tipe data
- Daftar belanja dengan operasi tambah/hapus item
- Hasil kalkulasi matematika sederhana

================================================================================
TUGAS 4 - Struktur Data Lanjutan
================================================================================

Fokus utama: Mendalami semua struktur data yang ada di Python.

Yang dipelajari:
1. LIST - Struktur data yang paling sering digunakan
   - Akses elemen dengan index (positif dan negatif)
   - Slicing untuk mengambil range elemen
   - Methods: append(), insert(), extend(), pop(), remove()

2. TUPLE - Seperti list tapi immutable (tidak bisa diubah)
   - Unpacking nilai ke variabel
   - Menggunakan *sisa untuk menangkap elemen yang tersisa

3. SET - Kumpulan unik tanpa duplikat
   - Union (|): Gabungan semua elemen
   - Intersection (&): Elemen yang sama di kedua set
   - Difference (-): Elemen di A tapi tidak di B
   - Symmetric Difference (^): Elemen yang berbeda

4. DICTIONARY - Key-value pairs seperti kamus
   - Menambah/mengubah key baru
   - Delete key
   - Iterasi dengan .keys(), .values(), .items()

5. NESTED STRUCTURE - Kombinasi list dan dictionary
   - Menyimpan data buku (judul, penulis, tahun)
   - List comprehension untuk filter data

Apa yang dibikin:
- Catatan harian dengan list manipulation
- Data mahasiswa dengan dictionary
- Database buku dengan nested structure
- List comprehension untuk generate bilangan genap dan kuadrat

================================================================================
TUGAS 5 - Object-Oriented Programming (OOP)
================================================================================

Fokus utama: Beranjak dari functional programming ke OOP.

Yang dipelajari:
- Functions dengan type hints
- Class dan constructor (__init__)
- Instance variables (self.nama, self.nilai, dll)
- Methods untuk operasi pada object
- String representation (__str__)
- Default parameters dalam method

Apa yang dibikin:
Class Student dengan fitur:
- Menyimpan nama dan npm mahasiswa
- Menambahkan nilai ujian
- Menghitung rata-rata nilai
- Menentukan status lulus/tidak lulus
- Display informasi student dalam format rapi

Contoh:
Seorang mahasiswa bernama Styven dengan nilai [95, 92] akan mendapat 
rata-rata 93.5 dan status "Lulus"

================================================================================
TUGAS 6 - NumPy, Pandas, dan Operasi Data Tabel
================================================================================

Fokus utama: Bekerja dengan data dalam skala lebih besar menggunakan library.

Yang dipelajari:
1. NumPy - Numerical Python untuk array operations
   - Generate random array (nilai ujian acak)
   - Statistik dasar: mean, median, standard deviation, min, max

2. Pandas - Data manipulation dan analysis
   - Membuat DataFrame dari dictionary
   - Kolom baru dengan np.where() untuk conditional logic
   - Viewing data dengan .head()

3. OOP untuk domain tertentu
   - Class GradeBook untuk manage nilai kelas
   - Methods untuk hitung average dan pass rate
   - Save summary ke file

4. File I/O
   - Write ke file dengan 'w' (create/overwrite)
   - Append ke file dengan 'a' (add content)
   - Reading dan processing file

Apa yang dibikin:
- Array 10 nilai ujian random (50-100)
- DataFrame berisi nama, NIM, nilai, status
- Perhitungan statistik (rata-rata, median, standar deviasi, min-max)
- Menentukan status "LULUS" untuk nilai >= 70
- Simpan ringkasan ke file ringkasan_tugas6.txt

Hasil statistik:
- Total 10 siswa dengan nilai bervariasi
- Perhitungan pass rate (berapa persen yang lulus)
- Summary disimpan ke file untuk dokumentasi

================================================================================
STRUKTUR FOLDER
================================================================================

tugas3.py          - Program dasar Python (tipe data, operasi, input)
tugas4.py          - Struktur data advanced (list, tuple, set, dict)
tugas5.py          - Implementasi OOP dengan class Student
tugas6.py          - NumPy, Pandas, dan data analysis
ringkasan_tugas6.txt - Output dari tugas 6 (statistik dan summary)
README.txt         - File ini, dokumentasi lengkap

================================================================================
PROGRESSION & LEARNING PATH
================================================================================

Dari Tugas 3 → 6, materi berkembang dari hal sederhana ke kompleks:

Tugas 3: Dasar-dasar (variabel, tipe data, input/output)
    ↓
Tugas 4: Struktur data (cara menyimpan banyak data)
    ↓
Tugas 5: Abstraksi (mengelompokkan data + operasinya dalam class)
    ↓
Tugas 6: Real-world application (menggunakan library untuk data di skala besar)

Setiap tugas membangun atas pengetahuan sebelumnya, menciptakan fondasi yang kuat 
untuk programming lebih lanjut.

================================================================================
CATATAN TEKNIS
================================================================================

- Semua program menggunakan Python 3
- Tugas 6 memerlukan library: numpy, pandas
- Semua output dicetak ke console dan beberapa disimpan ke file
- Type hints digunakan untuk clarity (terutama di Tugas 5-6)
- Seed 42 digunakan untuk reproducibility di numpy

================================================================================
TIPS UNTUK MENJALANKAN
================================================================================

Python 3.x harus terinstall di sistem.

Untuk tugas 3-5:
  python tugas3.py
  python tugas4.py
  python tugas5.py

Untuk tugas 6 (memerlukan library):
  pip install numpy pandas
  python tugas6.py

Program akan langsung menampilkan output dan membuat file jika ada operasi I/O.

================================================================================

Semoga dokumentasi ini membantu dalam memahami setiap tugas yang telah dikerjakan.
Jika ada yang ingin diperjelas atau dikembangkan lebih lanjut, silakan lanjutkan 
eksperimen dengan code! Itu adalah cara terbaik untuk belajar.

================================================================================
