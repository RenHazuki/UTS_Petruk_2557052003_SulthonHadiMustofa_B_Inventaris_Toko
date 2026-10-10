"""Class utama yang menggambarkan barang dan kumpulan inventaris."""

from .validasi import DataBarangError


class Barang:
    """Menyimpan atribut satu barang di toko."""

    def __init__(self, kode, nama, kategori, harga, stok):
        # Assert memeriksa asumsi internal bahwa stok selalu bilangan bulat.
        assert isinstance(stok, int) and not isinstance(stok, bool), (
            "Stok harus berupa bilangan bulat."
        )
        self.kode = str(kode)
        self.nama = str(nama)
        self.kategori = str(kategori)
        self.harga = float(harga)
        self.stok = stok

    def ke_baris(self):
        """Mengubah barang menjadi satu baris teks dengan pemisah titik koma."""
        return f"{self.kode};{self.nama};{self.kategori};{self.harga};{self.stok}"

    def nilai_persediaan(self):
        """Menghitung nilai uang seluruh stok barang ini."""
        return self.harga * self.stok


class Inventaris:
    """Mengelola sekumpulan objek Barang di memori."""

    def __init__(self, daftar_barang=None):
        self.daftar_barang = list(daftar_barang) if daftar_barang else []

    def cari(self, kode):
        """Mengembalikan barang dengan kode yang cocok, atau None jika tidak ada."""
        for barang in self.daftar_barang:
            if barang.kode.lower() == str(kode).strip().lower():
                return barang
        return None

    def tambah(self, barang):
        """Menambahkan barang selama kodenya belum digunakan."""
        if self.cari(barang.kode) is not None:
            raise DataBarangError(f"Kode barang {barang.kode} sudah digunakan.")
        self.daftar_barang.append(barang)
        return barang
