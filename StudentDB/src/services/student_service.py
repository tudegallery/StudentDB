from src.models.student import Student
from src.repository.student_repo import load_students, save_students
from src.utils.logger import log

def add_student(name, age, major):
    students = load_students()
    new_student = Student(name, age, major)
    students.append(new_student.to_dict())
    save_students(students)
    log(f"ADD STUDENT: {name}")

def view_students():
    students = load_students()
    return students

def update_student(name, new_age=None, new_major=None):
    students = load_students()
    for s in students:
        if s["name"] == name:
            if new_age:
                s["age"] = new_age
            if new_major:
                s["major"] = new_major
            save_students(students)
            log(f"UPDATE STUDENT: {name}")
            return True
    return False

def delete_student(name):
    students = load_students()
    new_list = [s for s in students if s["name"] != name]
    save_students(new_list)
    log(f"DELETE STUDENT: {name}")
