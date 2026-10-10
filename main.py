"""Program utama Inventaris Toko."""

from pathlib import Path

from inventaris.fileio import (
    buat_file_jika_belum_ada,
    baca_barang,
    tambahkan_barang,
    simpan_laporan,
)
from inventaris.models import Inventaris
from inventaris.processing import (
    buat_barang,
    cari_barang,
    analisis_inventaris,
    buat_teks_laporan,
)
from inventaris.validasi import DataBarangError

# Path dibuat berdasarkan lokasi main.py agar tetap benar walau terminal dibuka dari folder lain.
FOLDER_PROYEK = Path(__file__).resolve().parent
FILE_DATA = FOLDER_PROYEK / "data_barang.txt"
FILE_LAPORAN = FOLDER_PROYEK / "laporan_inventaris.txt"


def tampilkan_barang(daftar_barang):
    """Menampilkan daftar barang secara rapi."""
    if not daftar_barang:
        print("Belum ada data barang.")
        return

    print("\nDAFTAR BARANG")
    print("-" * 72)
    print(f"{'Kode':<10} {'Nama':<20} {'Kategori':<15} {'Harga':>12} {'Stok':>6}")
    print("-" * 72)
    for barang in sorted(daftar_barang, key=lambda item: item.nama.lower()):
        print(
            f"{barang.kode:<10} {barang.nama:<20} {barang.kategori:<15} "
            f"{barang.harga:>12,.2f} {barang.stok:>6}"
        )


def menu_tambah_barang():
    """Menerima input, memvalidasi, lalu menyimpan satu barang baru."""
    try:
        kode = input("Kode barang   : ").strip()
        nama = input("Nama barang   : ").strip()
        kategori = input("Kategori      : ").strip()
        harga = float(input("Harga barang  : Rp"))
        stok = int(input("Jumlah stok   : "))

        # Keyword arguments membuat maksud setiap nilai terlihat jelas.
        barang_baru = buat_barang(
            kode=kode,
            nama=nama,
            kategori=kategori,
            harga=harga,
            stok=stok,
        )

        inventaris = Inventaris(baca_barang(FILE_DATA))
        inventaris.tambah(barang_baru)

        if tambahkan_barang(FILE_DATA, barang_baru):
            print("Barang berhasil ditambahkan.")
    except (ValueError, DataBarangError) as error:
        print(f"Input tidak dapat diproses: {error}")


def menu_cari_barang():
    """Mencari barang berdasarkan kode, nama, atau kategori."""
    kata_kunci = input("Masukkan kode, nama, atau kategori: ").strip()
    hasil = cari_barang(baca_barang(FILE_DATA), kata_kunci)
    tampilkan_barang(hasil)


def menu_laporan():
    """Menganalisis persediaan, menyimpan laporan, dan menampilkannya."""
    daftar_barang = baca_barang(FILE_DATA)
    hasil = analisis_inventaris(daftar_barang, batas_stok_rendah=5)
    teks_laporan = buat_teks_laporan(daftar_barang, hasil)

    if simpan_laporan(FILE_LAPORAN, teks_laporan):
        print("\n" + teks_laporan)
        print(f"\nLaporan disimpan di: {FILE_LAPORAN}")


def main():
    """Menjalankan menu hingga pengguna memilih keluar."""
    buat_file_jika_belum_ada(FILE_DATA)

    while True:
        print("\n=== PROGRAM INVENTARIS TOKO ===")
        print("1. Lihat semua barang")
        print("2. Tambah barang")
        print("3. Cari barang")
        print("4. Analisis dan simpan laporan")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tampilkan_barang(baca_barang(FILE_DATA))
        elif pilihan == "2":
            menu_tambah_barang()
        elif pilihan == "3":
            menu_cari_barang()
        elif pilihan == "4":
            menu_laporan()
        elif pilihan == "5":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1 sampai 5.")


if __name__ == "__main__":
    main()
