# Russian Peasant Multiplication

![Russian Peasant](https://img.shields.io/badge/Algorithm-Russian%20Peasant%20Multiplication-green)
![Python Version](https://img.shields.io/badge/Python-3.x-blue)

## Deskripsi 
Russian Peasant Multiplication adalah sebuah algoritma kuno yang digunakan untuk mengalikan dua bilangan secara efisien dengan menggunakan pendekatan decrease-and-conquer. Algoritma ini terutama berguna dalam mengalikan bilangan besar menggunakan operasi penjumlahan dan pengurangan yang sederhana.

## Cara Kerja
Algoritma ini bekerja dengan cara mengurangi satu bilangan secara berulang kali hingga mencapai nol, sementara bilangan lainnya dikalikan dengan 2 dalam setiap iterasi. Hasil perkalian dari bilangan yang tidak diubah ini kemudian dijumlahkan untuk mendapatkan hasil akhir.

## Cara Penggunaan
1. Pastikan Python telah terinstal di komputer Anda.
2. Clone repositori ini ke lokal komputer Anda.
   ```bash
   git clone https://github.com/username/repo.git
   ```
3. Masuk ke direktori repo.
   ```bash
   cd repo
   ```
4. Jalankan program dengan menjalankan script Python `russian_peasant_multiplication.py`.
   ```bash
   python russian_peasant_multiplication.py
   ```
5. Program akan meminta Anda untuk memasukkan dua bilangan yang ingin dikalikan. Masukkan bilangan sesuai keinginan Anda dan tekan Enter.
6. Hasil perkalian dari kedua bilangan akan ditampilkan di layar beserta dengan langkah-langkah perhitungan.

## Contoh Penggunaan
```bash
Masukkan bilangan pertama: 15
Masukkan bilangan kedua: 12
Hasil perkalian dari 15 dan 12 adalah: 180

Langkah-langkah perhitungan:
a dibagi 2: 7, b dikalikan 2: 24
12 ditambahkan karena 7 ganjil
a dibagi 2: 3, b dikalikan 2: 48
48 ditambahkan karena 3 ganjil
a dibagi 2: 1, b dikalikan 2: 96
```

## Analisis Kebutuhan Waktu
- **Analisis Operasi/Instruksi:** Algoritma ini terdiri dari operasi dasar seperti penjumlahan, pembagian, dan perkalian. Jumlah operasi akan sekitar `O(n)`, dengan `n` adalah jumlah bit yang diperlukan untuk merepresentasikan bilangan terbesar.
  
- **Analisis Jumlah Operasi:** Jumlah operasi dalam algoritma ini sebanding dengan logaritma basis 2 dari bilangan terbesar yang diinputkan. Jumlah operasi adalah `O(log n)`.

- **Analisis Kasus Terbaik, Terburuk, dan Rata-rata:** Kompleksitas waktu dalam kasus terbaik, terburuk, dan rata-rata adalah `O(log n)`.

