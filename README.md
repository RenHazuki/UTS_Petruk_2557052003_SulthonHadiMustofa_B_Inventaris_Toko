# UTS Pemrograman Terstruktur — Bagian B
## Proyek: Inventaris Toko

Program terminal sederhana untuk mencatat barang toko, mencari barang, menganalisis persediaan, menyimpan laporan, dan menguji fungsi pengolahan data.

## Fitur
- Menampilkan data barang.
- Menambahkan barang baru dengan validasi.
- Mencari barang berdasarkan kode, nama, atau kategori.
- Menghitung total stok dan nilai persediaan.
- Menampilkan barang termahal, termurah, dan stok rendah.
- Menyimpan hasil analisis ke `laporan_inventaris.txt`.
- Melewati baris data rusak dan menampilkan peringatan.

## Struktur folder

```text
UTS_B_Inventaris_Toko/
├── main.py
├── README.md
├── LAPORAN_BAGIAN_B.md
└── inventaris/
    ├── __init__.py
    ├── models.py
    ├── validasi.py
    ├── fileio.py
    ├── processing.py
    └── testing.py
```

`data_barang.txt` akan dibuat otomatis saat program pertama kali dijalankan. File laporan dibuat saat menu nomor 4 dipilih.

## Cara menjalankan
Pastikan Python 3 terpasang. Buka terminal pada folder proyek, lalu jalankan:

```powershell
python main.py
```

## Cara menjalankan pengujian
Dari folder yang sama, jalankan:

```powershell
python -m unittest inventaris.testing -v
```

Ada tujuh pengujian untuk total stok, nilai persediaan, barang termahal, filter stok rendah, pembuatan objek dengan keyword arguments, penolakan stok negatif, dan analisis data kosong.

## Penerapan konsep yang diminta
- **Class:** `Barang` dan `Inventaris` pada `models.py`.
- **Fungsi buatan:** tersebar pada modul untuk validasi, file handling, pencarian, analisis, dan laporan.
- **`*args`:** `hitung_total_stok(*jumlah_stok)`.
- **`**kwargs`:** `buat_barang(**data)`.
- **`lambda`:** digunakan untuk mengurutkan barang dan memilih barang berdasarkan harga atau stok.
- **Keyword argument:** pemanggilan `buat_barang(kode=..., nama=..., ...)` dan `analisis_inventaris(..., batas_stok_rendah=5)`.
- **Modularitas:** package `inventaris` dengan `__init__.py` dan lima modul lain.
- **File handling:** `x` untuk membuat file tanpa menimpa, `a` untuk menambahkan data, `r` untuk membaca iteratif, dan `w` untuk mengganti isi laporan. Semua operasi file memakai `with open()`.
- **Debugging:** `try/except` menangani input dan baris rusak; `raise` digunakan lewat `DataBarangError`; `assert` memeriksa asumsi bahwa stok di dalam objek merupakan integer.
- **Unit testing:** `unittest`, satu class `TestInventaris`, dan tujuh metode pengujian.
- **Refactoring:** lihat tabel pada `LAPORAN_BAGIAN_B.md`.
