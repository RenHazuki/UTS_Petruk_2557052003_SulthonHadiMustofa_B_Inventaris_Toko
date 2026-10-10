"""Fungsi untuk membuat, mencari, dan menganalisis data inventaris."""

from .models import Barang
from .validasi import validasi_barang


def buat_barang(**data):
    """Membuat objek Barang dari atribut yang dikirim sebagai keyword arguments."""
    atribut_wajib = {"kode", "nama", "kategori", "harga", "stok"}
    if not atribut_wajib.issubset(data):
        kurang = ", ".join(sorted(atribut_wajib - set(data)))
        raise ValueError(f"Atribut wajib belum lengkap: {kurang}.")

    data_valid = validasi_barang(
        kode=data["kode"],
        nama=data["nama"],
        kategori=data["kategori"],
        harga=data["harga"],
        stok=data["stok"],
    )
    return Barang(**data_valid)


def hitung_total_stok(*jumlah_stok):
    """Menjumlahkan berapa pun jumlah angka stok yang diberikan melalui *args."""
    for jumlah in jumlah_stok:
        if not isinstance(jumlah, int) or isinstance(jumlah, bool) or jumlah < 0:
            raise ValueError("Setiap stok harus berupa bilangan bulat nonnegatif.")
    return sum(jumlah_stok)


def filter_stok_rendah(daftar_barang, batas=5):
    """Mengambil barang yang stoknya sama dengan atau di bawah batas yang ditentukan."""
    barang_rendah = [barang for barang in daftar_barang if barang.stok <= batas]
    return sorted(barang_rendah, key=lambda barang: barang.stok)


def cari_barang(daftar_barang, kata_kunci):
    """Mencari kode, nama, atau kategori barang tanpa membedakan huruf besar-kecil."""
    kata_kunci = str(kata_kunci).strip().lower()
    return [
        barang for barang in daftar_barang
        if kata_kunci in barang.kode.lower()
        or kata_kunci in barang.nama.lower()
        or kata_kunci in barang.kategori.lower()
    ]


def analisis_inventaris(daftar_barang, batas_stok_rendah=5):
    """Menghasilkan ringkasan jumlah barang, total stok, nilai persediaan, dan stok rendah."""
    total_stok = hitung_total_stok(*(barang.stok for barang in daftar_barang))
    total_nilai = sum(barang.nilai_persediaan() for barang in daftar_barang)

    if daftar_barang:
        barang_termahal = max(daftar_barang, key=lambda barang: barang.harga)
        barang_termurah = min(daftar_barang, key=lambda barang: barang.harga)
    else:
        barang_termahal = None
        barang_termurah = None

    return {
        "jumlah_jenis_barang": len(daftar_barang),
        "total_stok": total_stok,
        "total_nilai_persediaan": total_nilai,
        "barang_termahal": barang_termahal,
        "barang_termurah": barang_termurah,
        "stok_rendah": filter_stok_rendah(daftar_barang, batas=batas_stok_rendah),
    }


def buat_teks_laporan(daftar_barang, hasil):
    """Menyusun ringkasan analisis menjadi teks yang siap disimpan sebagai laporan."""
    baris = [
        "LAPORAN INVENTARIS TOKO",
        "=" * 24,
        f"Jumlah jenis barang : {hasil['jumlah_jenis_barang']}",
        f"Total seluruh stok  : {hasil['total_stok']}",
        f"Nilai persediaan    : Rp{hasil['total_nilai_persediaan']:,.2f}",
    ]

    if hasil["barang_termahal"] is not None:
        barang = hasil["barang_termahal"]
        baris.append(f"Barang termahal     : {barang.nama} (Rp{barang.harga:,.2f})")
        barang = hasil["barang_termurah"]
        baris.append(f"Barang termurah     : {barang.nama} (Rp{barang.harga:,.2f})")
    else:
        baris.append("Belum ada data barang.")

    baris.append("")
    baris.append("DAFTAR BARANG")
    baris.append("-" * 40)
    if daftar_barang:
        # Lambda digunakan untuk mengurutkan barang berdasarkan nama.
        for barang in sorted(daftar_barang, key=lambda item: item.nama.lower()):
            baris.append(
                f"{barang.kode} | {barang.nama} | {barang.kategori} | "
                f"Harga: Rp{barang.harga:,.2f} | Stok: {barang.stok}"
            )
    else:
        baris.append("Belum ada barang untuk ditampilkan.")

    baris.append("")
    baris.append("BARANG DENGAN STOK RENDAH (batas 5)")
    baris.append("-" * 40)
    if hasil["stok_rendah"]:
        for barang in hasil["stok_rendah"]:
            baris.append(f"{barang.nama} - tersisa {barang.stok}")
    else:
        baris.append("Tidak ada barang dengan stok rendah.")

    return "\n".join(baris)
