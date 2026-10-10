# Laporan Proyek Mandiri — Inventaris Toko

## 1. Deskripsi Program

Program Inventaris Toko dibuat untuk membantu pencatatan barang secara sederhana melalui terminal. Pengguna dapat melihat daftar barang, menambahkan barang, mencari barang berdasarkan kode/nama/kategori, dan membuat laporan persediaan. Data utama disimpan di file teks sehingga dapat dibaca kembali saat program dijalankan lagi.

## 2. Alur Program

1. Program memeriksa file `data_barang.txt`. Jika belum ada, program membuatnya menggunakan mode `x` tanpa menimpa file yang sudah ada.
2. Pengguna memilih salah satu menu.
3. Saat menambahkan barang, program membaca input, memeriksa tipe dan isi data, menolak kode yang sudah digunakan, lalu menyimpan barang dengan mode `a`.
4. Saat menampilkan atau mencari barang, program membaca file dengan mode `r` baris demi baris. Baris yang tidak sesuai format atau mempunyai nilai tidak valid dilewati dan diberi pesan peringatan.
5. Saat membuat laporan, program menghitung jumlah jenis barang, total stok, nilai persediaan, barang termahal dan termurah, serta daftar stok rendah.
6. Laporan ditulis ke `laporan_inventaris.txt` menggunakan mode `w` dan ditampilkan pada terminal.

## 3. Pembagian Modul

- `models.py`: class `Barang` untuk menyimpan data satu barang dan class `Inventaris` untuk mengelola kumpulan barang.
- `validasi.py`: pemeriksaan kolom wajib, harga, stok, dan karakter pemisah. Modul ini memiliki exception buatan `DataBarangError`.
- `fileio.py`: membuat, membaca, dan menulis file data serta laporan.
- `processing.py`: membuat objek barang, menghitung stok, mencari barang, memfilter stok rendah, menganalisis data, dan menyusun laporan.
- `testing.py`: menjalankan unit test menggunakan `unittest`.
- `main.py`: menyediakan menu dan menghubungkan modul-modul.

## 4. Penerapan Materi

Program memiliki dua class, yaitu `Barang` dan `Inventaris`, serta beberapa fungsi buatan untuk validasi, pembacaan file, pencarian, perhitungan, analisis, dan pelaporan. `*args` dipakai pada `hitung_total_stok()` agar fungsi menerima jumlah stok dalam jumlah berbeda. `**kwargs` dipakai pada `buat_barang()` agar atribut barang dapat dikirim sebagai pasangan nama dan nilai. `lambda` digunakan untuk memilih atau mengurutkan data berdasarkan atribut barang. Keyword argument digunakan saat fungsi dipanggil agar arti setiap argumen jelas.

Keempat mode file yang diminta diterapkan dengan `with open()`. Mode `x` membuat file data baru tanpa menimpa file yang sudah ada; mode `a` menambahkan record; mode `r` membaca baris demi baris; mode `w` menggantikan isi file laporan. `FileExistsError` ditangani saat file sudah ada dan `FileNotFoundError` ditangani saat file data tidak tersedia. Kesalahan konversi atau format pada satu baris ditangani dengan `try/except`, lalu baris tersebut dilewati. `raise` dipakai untuk memunculkan `DataBarangError` pada data yang tidak sesuai. `assert` memeriksa bahwa stok yang masuk ke objek `Barang` berupa integer.

## 5. Tabel Refactoring

| Sebelum diperbaiki | Setelah diperbaiki | Teknik refactoring | Alasan |
|---|---|---|---|
| Proses membaca, mengolah, dan menampilkan data berpotensi ditulis dalam satu file panjang. | Proses dipisah ke `fileio.py`, `processing.py`, `validasi.py`, dan `models.py`. | Extract Module / pemisahan tanggung jawab | Kode lebih mudah dibaca, diuji, dan dikembangkan. |
| Validasi dan pembuatan data barang bisa diulang di beberapa bagian program. | Pemeriksaan disatukan dalam `validasi_barang()` dan pembuatan objek melalui `buat_barang()`. | Extract Function | Aturan validasi cukup dirawat di satu tempat. |
| Penjumlahan stok dan pencarian barang dapat ditulis ulang ketika dibutuhkan. | Dibuat fungsi `hitung_total_stok()`, `cari_barang()`, dan `analisis_inventaris()`. | Extract Function | Fungsi dapat digunakan kembali sehingga pengulangan berkurang. |
| Data barang berpotensi disimpan dan dikelola menggunakan susunan data yang tidak konsisten. | Data satu barang disusun dalam class `Barang`, sedangkan kumpulan barang dikelola oleh `Inventaris`. | Encapsulate / pengelompokan data | Struktur data lebih jelas dan operasi lebih teratur. |
| Nama variabel umum dapat membingungkan pembaca. | Menggunakan nama seperti `daftar_barang`, `batas_stok_rendah`, dan `total_nilai_persediaan`. | Rename Variable | Nama lebih menjelaskan maksud variabel. |

## 6. Pengujian

Pengujian dijalankan dengan perintah:

```powershell
python -m unittest inventaris.testing -v
```

Tujuh pengujian memeriksa total stok, total nilai persediaan, pemilihan barang termahal, filter stok rendah, pembuatan barang menggunakan keyword arguments, penolakan stok negatif, dan analisis ketika belum ada barang. Pengujian dinyatakan berhasil jika seluruh assertion terpenuhi.

## 7. Lampiran yang Perlu Ditambahkan Saat Pengumpulan

- Tautan repository publik yang berisi seluruh source code.
- Tautan video presentasi publik.
- Screenshot input/menu program dan contoh output.
- Screenshot kode dari class, fungsi pemrosesan, file handling, validasi, serta unit testing.

Tautan repository dan video perlu diisi setelah proyek diunggah oleh mahasiswa.
