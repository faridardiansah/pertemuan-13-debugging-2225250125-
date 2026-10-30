# Praktik 4: Investigasi dan Perbaikan Bug

def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)

def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    tertinggi = nilai[0]
    for x in nilai:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


# Data mahasiswa
nilai = [80, 60, 90, 70]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))


# Test Case
print("\n=== HASIL TEST CASE ===")

print("T1:", "PASS" if hitung_rata_rata([80, 60, 90, 70]) == 75.0 else "FAIL")
print("T2:", "PASS" if hitung_rata_rata([100, 80]) == 90.0 else "FAIL")
print("T3:", "PASS" if status(60) == "Lulus" else "FAIL")
print("T4:", "PASS" if status(59) == "Tidak lulus" else "FAIL")
print("T5:", "PASS" if nilai_tertinggi([80, 60, 90, 70]) == 90 else "FAIL")