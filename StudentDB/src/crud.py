import json
import logging
import os
from datetime import datetime
from src.database import load_data, save_data

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_id(data):
    """Buat ID unik berdasarkan data terakhir."""
    if not data:
        return 1
    return max([s["id"] for s in data]) + 1

def add_student():
    """Tambah data mahasiswa baru."""
    data = load_data() or []

    print("\n=== Tambah Data Mahasiswa ===")
    try:
        name = input("Nama: ").strip()
        age = int(input("Umur: "))
        major = input("Jurusan: ").strip()

        new_student = {
            "id": generate_id(data),
            "name": name,
            "age": age,
            "major": major,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data.append(new_student)
        save_data(data)
        logging.info(f"ADD STUDENT: {name}")
        print(f"Mahasiswa '{name}' berhasil ditambahkan!")
    except ValueError:
        print("Umur harus berupa angka!")


def view_students():
    """Tampilkan seluruh data mahasiswa."""
    data = load_data() or []

    print("\n=== Daftar Mahasiswa ===")
    if not data:
        print("Belum ada data.")
        return

    for s in data:
        print(f"[{s['id']}] {s['name']} - {s['major']} ({s['age']} tahun)")


def delete_student():
    """Hapus data mahasiswa berdasarkan ID."""
    data = load_data() or []
    if not data:
        print("Tidak ada data untuk dihapus.")
        return

    try:
        sid = int(input("Masukkan ID mahasiswa yang ingin dihapus: "))
        found = next((s for s in data if s["id"] == sid), None)

        if found:
            data.remove(found)
            save_data(data)
            logging.info(f"DELETE STUDENT: {found['name']}")
            print(f"Mahasiswa '{found['name']}' berhasil dihapus!")
        else:
            print("ID tidak ditemukan.")
    except ValueError:
        print("Masukkan ID berupa angka.")


def update_student():
    """Update data mahasiswa (umur/jurusan)."""
    data = load_data() or []
    if not data:
        print("Tidak ada data untuk diperbarui.")
        return

    try:
        sid = int(input("Masukkan ID mahasiswa yang ingin diubah: "))
        found = next((s for s in data if s["id"] == sid), None)

        if not found:
            print("ID tidak ditemukan.")
            return

        print(f"\nEdit data untuk: {found['name']}")
        new_age = input(f"Umur baru ({found['age']}): ").strip()
        new_major = input(f"Jurusan baru ({found['major']}): ").strip()

        if new_age:
            found["age"] = int(new_age)
        if new_major:
            found["major"] = new_major

        save_data(data)
        logging.info(f"UPDATE STUDENT: {found['name']}")
        print(f"Data '{found['name']}' berhasil diperbarui!")

    except ValueError:
        print("Input tidak valid! Pastikan umur berupa angka.")
