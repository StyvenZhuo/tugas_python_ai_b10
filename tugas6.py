import numpy as np
import pandas as pd
import os

np.random.seed(42)

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return float(self.df['nilai'].mean())
    
    def pass_rate(self, threshold: float = 70.0) -> float:
        # Menghitung persentase siswa yang lulus berdasarkan threshold
        lulus_count = (self.df['nilai'] >= threshold).sum()
        persentase = (lulus_count / len(self.df)) * 100
        return float(persentase)
        
    def save_summary(self, path: str):
        # Menggunakan mode 'a' (append) agar menambah di baris baru
        with open(path, "a") as f:
            f.write("\n=== OOP: GRADEBOOK SUMMARY ===\n")
            f.write(f"Total Data  : {len(self.df)}\n")
            f.write(f"Rata-rata   : {self.average():.2f}\n")
            f.write(f"Pass Rate   : {self.pass_rate():.2f}%\n")
            
    def __str__(self):
        return f"GradeBook(Jumlah Data={len(self.df)}, Rata-rata Nilai={self.average():.2f})"
    
if __name__ == "__main__":
    nilai_ujian = np.random.randint(50, 101, size=10)
    print(f"Array Nilai Ujian: {nilai_ujian}")

    mean_val = np.mean(nilai_ujian)
    median_val = np.median(nilai_ujian)
    std_val = np.std(nilai_ujian)
    min_val = np.min(nilai_ujian)
    max_val = np.max(nilai_ujian)
    
    print(f"Rata-rata       : {mean_val:.2f}")
    print(f"Median          : {median_val:.2f}")
    print(f"Standar Deviasi : {std_val:.2f}")
    print(f"Nilai Min       : {min_val}")
    print(f"Nilai Max       : {max_val}")

    data = {
        'nama': ['Budi', 'Siti', 'Agus', 'Dewi', 'Andi', 'Rina', 'Joko', 'Maya', 'Doni', 'Lia'],
        'nim': [f"A{str(i).zfill(3)}" for i in range(1, 11)],
        'nilai': nilai_ujian
    }
    df = pd.DataFrame(data)
    
    # Tambah kolom status, gunakan np.where sebagai ganti apply/lambda agar lebih cepat
    df['status'] = np.where(df['nilai'] >= 70, 'LULUS', 'TIDAK LULUS')
    
    # Menampilkan 5 baris pertama DataFrame
    print(df.head())   


    # I/O

    file_path = "ringkasan_tugas6.txt"
    # Menggunakan 'w' (write) untuk menimpa/membuat file baru
    with open(file_path, "w") as f:
        f.write("=== RINGKASAN STATISTIK NUMPY ===\n")
        f.write(f"Rata-rata       : {mean_val:.2f}\n")
        f.write(f"Median          : {median_val:.2f}\n")
        f.write(f"Standar Deviasi : {std_val:.2f}\n")
        f.write(f"Nilai Min       : {min_val}\n")
        f.write(f"Nilai Max       : {max_val}\n")
        
        f.write("\n=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah Baris    : {len(df)}\n")
        jml_lulus = (df['status'] == 'LULUS').sum()
        jml_tdk_lulus = (df['status'] == 'TIDAK LULUS').sum()
        f.write(f"Jumlah Lulus    : {jml_lulus}\n")
        f.write(f"Jumlah Tdk Lulus: {jml_tdk_lulus}\n")
    
    gb = GradeBook(df)
    print(gb)
    print(f"Average   : {gb.average():.2f}")
    print(f"Pass Rate : {gb.pass_rate():.2f}%")
    
    # Panggil method save_summary (akan me-append ke file txt tadi)
    gb.save_summary(file_path)
    
    print(f"\n[INFO] File '{file_path}' berhasil dibuat dan disimpan di direktori saat ini.")