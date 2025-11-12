import json
from datetime import datetime
import os

DB_FILE = "students.json"

def load_data():
    """Load JSON data dari file, return list kosong jika belum ada."""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("⚠️ File JSON rusak, buat ulang.")
                return []
    return []

def save_data(data):
    """Simpan data ke file JSON."""
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_id(data):
    """Generate ID unik berdasarkan data terakhir."""
    if not data:
        return 1
    last_id = max([s["id"] for s in data])
    return last_id + 1

def add_student(data):
    """Menambahkan siswa baru ke database."""
    print("\n=== Tambah Siswa Baru ===")
    name = input("Nama siswa: ").strip()
    age = int(input("Umur: "))
    major = input("Jurusan: ").strip()

    student = {
        "id": generate_id(data),
        "name": name,
        "age": age,
        "major": major,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(student)
    save_data(data)
    print(f"✅ Data '{name}' berhasil ditambahkan!")

def view_students(data):
    """Menampilkan daftar siswa."""
    print("\n=== DAFTAR SISWA ===")
    if not data:
        print("❌ Belum ada data siswa.")
        return
    for s in data:
        print(f"[{s['id']}] {s['name']} - {s['major']} ({s['age']} tahun)")

def delete_student(data):
    """Menghapus data siswa berdasarkan ID."""
    try:
        sid = int(input("Masukkan ID siswa yang akan dihapus: "))
        found = next((s for s in data if s["id"] == sid), None)
        if found:
            data.remove(found)
            save_data(data)
            print(f"Data '{found['name']}' berhasil dihapus!")
        else:
            print("ID tidak ditemukan.")
    except ValueError:
        print("Masukkan ID berupa angka.")

def main():
    data = load_data()

    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tambah siswa")
        print("2. Lihat semua siswa")
        print("3. Hapus siswa")
        print("4. Keluar")
        choice = input("Pilih menu (1-4): ").strip()

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            delete_student(data)
        elif choice == "4":
            print("Keluar program")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
