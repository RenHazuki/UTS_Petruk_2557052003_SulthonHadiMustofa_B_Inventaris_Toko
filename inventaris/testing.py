"""Unit test untuk fungsi pengolahan inventaris. Jalankan dengan python -m unittest inventaris.testing."""

import unittest

from .models import Barang
from .processing import (
    buat_barang,
    hitung_total_stok,
    analisis_inventaris,
    filter_stok_rendah,
)
from .validasi import DataBarangError


class TestInventaris(unittest.TestCase):
    """Menguji hasil perhitungan dan validasi inventaris."""

    def setUp(self):
        # Data contoh dipakai ulang oleh setiap metode pengujian.
        self.barang = [
            Barang("A001", "Buku Tulis", "ATK", 5000, 10),
            Barang("A002", "Pulpen", "ATK", 3000, 2),
            Barang("B001", "Tas", "Aksesori", 75000, 1),
        ]

    def test_total_stok(self):
        self.assertEqual(hitung_total_stok(10, 2, 1), 13)

    def test_nilai_total_persediaan(self):
        hasil = analisis_inventaris(self.barang)
        self.assertAlmostEqual(hasil["total_nilai_persediaan"], 131000)

    def test_barang_termahal(self):
        hasil = analisis_inventaris(self.barang)
        self.assertEqual(hasil["barang_termahal"].nama, "Tas")

    def test_filter_stok_rendah(self):
        hasil = filter_stok_rendah(self.barang, batas=5)
        self.assertEqual([item.nama for item in hasil], ["Tas", "Pulpen"])

    def test_buat_barang_dengan_keyword_argument(self):
        barang = buat_barang(
            kode="C001",
            nama="Penghapus",
            kategori="ATK",
            harga=2000,
            stok=4,
        )
        self.assertEqual(barang.nama, "Penghapus")
        self.assertEqual(barang.stok, 4)

    def test_stok_negatif_ditolak(self):
        with self.assertRaises(DataBarangError):
            buat_barang(
                kode="C002",
                nama="Penggaris",
                kategori="ATK",
                harga=4000,
                stok=-1,
            )

    def test_analisis_data_kosong(self):
        hasil = analisis_inventaris([])
        self.assertEqual(hasil["jumlah_jenis_barang"], 0)
        self.assertEqual(hasil["total_stok"], 0)
        self.assertIsNone(hasil["barang_termahal"])


if __name__ == "__main__":
    unittest.main()
