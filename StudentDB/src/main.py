import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.crud import add_student, view_students, delete_student, update_student
from src.database import load_data, save_data

def main():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Update Data Mahasiswa")
        print("5. Keluar Program")

        choice = input("Pilih menu (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            print("Keluar program.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()

