"""Validasi data barang sebelum disimpan atau diproses."""


class DataBarangError(ValueError):
    """Error khusus untuk data barang yang tidak sesuai aturan."""


def validasi_barang(kode, nama, kategori, harga, stok):
    """Memeriksa kelengkapan dan tipe data barang, lalu mengembalikan data yang rapi."""
    kode = str(kode).strip()
    nama = str(nama).strip()
    kategori = str(kategori).strip()

    if not kode or not nama or not kategori:
        raise DataBarangError("Kode, nama, dan kategori tidak boleh kosong.")

    # Tanda titik koma dipakai sebagai pemisah kolom di file data.
    if any(";" in nilai for nilai in (kode, nama, kategori)):
        raise DataBarangError("Kode, nama, dan kategori tidak boleh berisi titik koma.")

    try:
        harga = float(harga)
        stok = int(stok)
    except (TypeError, ValueError) as error:
        raise DataBarangError("Harga harus berupa angka dan stok harus berupa bilangan bulat.") from error

    if harga < 0:
        raise DataBarangError("Harga tidak boleh negatif.")
    if stok < 0:
        raise DataBarangError("Stok tidak boleh negatif.")

    return {
        "kode": kode,
        "nama": nama,
        "kategori": kategori,
        "harga": harga,
        "stok": stok,
    }
