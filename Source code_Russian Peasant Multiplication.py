def RussianPeasantMultiplication(a, b):
    # Inisialisasi hasil
    result = 0

    # Inisialisasi list untuk menyimpan langkah-langkah perhitungan
    steps = []

    # Proses algoritma
    while a > 0:
        if a % 2 != 0:
            # Jika a ganjil, tambahkan b ke dalam hasil
            result += b
            # Simpan langkah penambahan ke dalam list
            steps.append(f"{b} ditambahkan karena {a} ganjil")
        # Bagi a dengan 2 dan kali b dengan 2
        a //= 2
        b *= 2
        # Simpan langkah pembagian dan perkalian ke dalam list
        steps.append(f"a dibagi 2: {a}, b dikalikan 2: {b}")

    return result, steps

# Input pengguna
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

# Memanggil fungsi RussianPeasantMultiplication dengan input pengguna
result, steps = RussianPeasantMultiplication(num1, num2)

# Cetak hasil perkalian
print(f"Hasil perkalian dari {num1} dan {num2} adalah: {result}")

# Cetak langkah-langkah perhitungan
print("\nLangkah-langkah perhitungan:")
for step in steps:
    print(step)