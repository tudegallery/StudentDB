from src.database import load_data, save_data
from src.validation import validate_student
from Development.Python.StudentDB.src.utils.logger import log

def add_student():
    students = load_data()
    name = input("Masukkan nama mahasiswa: ").strip()
    age = int(input("Masukkan umur: "))
    major = input("Masukkan jurusan: ").strip()

    student = {"name": name, "age": age, "major": major}
    validate_student(student)
    students.append(student)
    save_data(students)
    log(f"ADD STUDENT: {name}")

def view_students():
    students = load_data()
    if not students:
        print("Belum ada data mahasiswa.")
        return
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} - {s['age']} tahun - {s['major']}")

def delete_student():
    students = load_data()
    name = input("Masukkan nama mahasiswa yang ingin dihapus: ").strip()
    updated = [s for s in students if s["name"].lower() != name.lower()]
    if len(updated) == len(students):
        print("Mahasiswa tidak ditemukan.")
        return
    save_data(updated)
    log(f"DELETE STUDENT: {name}")

def update_student():
    students = load_data()
    name = input("Masukkan nama mahasiswa yang ingin diupdate: ").strip()
    found = False
    for s in students:
        if s["name"].lower() == name.lower():
            s["age"] = int(input("Masukkan umur baru: "))
            s["major"] = input("Masukkan jurusan baru: ").strip()
            found = True
            log(f"UPDATE STUDENT: {name}")
    if not found:
        print("Mahasiswa tidak ditemukan.")
    else:
        save_data(students)
        print(f"Data {name} berhasil diupdate.")