def greet(nama: str) -> str:
    return f"Hello, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return float(a+b)

def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)

class Student:
    def __init__(self, nama: str, npm: str):
        self.nama = nama
        self.npm = npm
        self.nilai: list[float] = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_rata_nilai(self) -> float:
        return rata_rata(self.nilai)
    
    def status(self, threshold: float = 70.0) -> str:
        if self.rata_rata_nilai() >= threshold:
            return "Lulus"
        else:
            return "Tidak Lulus"
            
    def __str__(self):
        return f"Student(nama='{self.nama}', npm='{self.npm}', nilai={self.nilai}), status={self.status()}"
    
if __name__ == "__main__":
    mhs1 = Student("Styven", "2331165")
    mhs1.tambah_nilai(95)
    mhs1.tambah_nilai(92)

    mhs2 = Student("Kennedi", "2331001")
    mhs2.tambah_nilai(90)
    mhs2.tambah_nilai(85)

    print(mhs1)
    print(f"Rata rata Nilai : {mhs1.rata_rata_nilai()}, Status : {mhs1.status()}")

    print(mhs2)
    print(f"Rata rata Nilai : {mhs2.rata_rata_nilai()}, Status : {mhs2.status()}")