from Human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book=None):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
    # def is_str_about_strudent(self, comparison_string=None):
    #     if comparison_string in self.__dict__.values():
    #         print(Student)
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.gender}, {self.age} y.o."

# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st1.is_str_about_strudent('Steve')
# st1.is_str_about_strudent(30)
# st1.is_str_about_strudent(32)
# st1.is_str_about_strudent('Steve')
