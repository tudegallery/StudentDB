from datetime import datetime

class Student:
    def __init__(self, id, name, age, major):
        self.id = id
        self.name = name
        self.age = age
        self.major = major
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "major": self.major,
            "created_at": self.created_at
        }
