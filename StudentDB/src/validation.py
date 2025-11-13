def validate_student(student):
    if not student.get("name"):
        raise ValueError("Nama mahasiswa wajib diisi!")
    if not isinstance(student.get("age"), int) or student["age"] <= 0:
        raise ValueError("Umur harus berupa angka positif.")
    if not student.get("major"):
        raise ValueError("Jurusan wajib diisi!")
    return True
