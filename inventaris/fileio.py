"""Semua operasi file data dan laporan inventaris."""

from .processing import buat_barang


def buat_file_jika_belum_ada(nama_file):
    """Membuat file data kosong dengan mode x; file lama tidak akan tertimpa."""
    try:
        with open(nama_file, "x", encoding="utf-8"):
            pass
        print(f"File data dibuat: {nama_file}")
    except FileExistsError:
        # File sudah ada sehingga isinya dibiarkan tetap utuh.
        pass


def baca_barang(nama_file):
    """Membaca file secara iteratif; baris rusak dilewati dan file yang hilang dilaporkan."""
    daftar_barang = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                if not baris.strip():
                    continue
                try:
                    bagian = baris.strip().split(";")
                    if len(bagian) != 5:
                        raise ValueError("Jumlah kolom bukan lima.")
                    kode, nama, kategori, harga, stok = bagian
                    barang = buat_barang(
                        kode=kode,
                        nama=nama,
                        kategori=kategori,
                        harga=harga,
                        stok=stok,
                    )
                    daftar_barang.append(barang)
                except (ValueError, TypeError) as error:
                    print(f"Peringatan: baris {nomor} dilewati ({error}).")
    except FileNotFoundError:
        print(f"Error: file data '{nama_file}' belum ada.")
    return daftar_barang


def tambahkan_barang(nama_file, barang):
    """Menambahkan satu record baru di akhir file menggunakan mode a."""
    try:
        with open(nama_file, "a", encoding="utf-8") as file:
            file.write(barang.ke_baris() + "\n")
        return True
    except OSError as error:
        print(f"Gagal menyimpan barang: {error}")
        return False


def simpan_laporan(nama_file, isi_laporan):
    """Menulis laporan dengan mode w, sehingga laporan lama digantikan."""
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write(isi_laporan)
        return True
    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
        return False
