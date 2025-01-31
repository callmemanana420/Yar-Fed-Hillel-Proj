from Human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book=None):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.gender}, {self.age} y.o."