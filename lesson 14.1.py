class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.gender}, {self.age} y.o."

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book=None):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.gender}, {self.age} y.o."

class AddTenPlusError(Exception):
    pass
class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
    def add_student(self, student: Student):
        if len(self.group) + 1 > 10:
            raise AddTenPlusError(f"AddTenPlusError: В этой группе уже 10 учеников")
        self.group.add(student)
    def delete_student(self, last_name):
        self.group = list(self.group)
        index_delete = None
        for i in range(len(self.group)):
            if self.group[i].last_name == last_name:
                index_delete = i
                break
        if index_delete is not None:
            self.group.pop(index_delete)
        self.group = set(self.group)
    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
    def __str__(self):
        all_students = ", ".join([f"{i.first_name} {i.last_name}" for i in self.group])
        return f'Number: {self.number}\nStudents: {all_students}'
        # return f'{len(self.group)}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student), 'Метод поиска должен возвращать экземпляр'
gr.delete_student('Taylor')
print(gr)  # Only one student
gr.delete_student('Taylor')  # No error!

gr_try = Group('try test group')
gr_try.add_student(st1)
gr_try.add_student(st2)
st3 = Student('Male', 22, 'John', 'Doe', 'AN150')
gr_try.add_student(st3)
st4 = Student('Female', 28, 'Anna', 'Smith', 'AN155')
gr_try.add_student(st4)
st5 = Student('Male', 26, 'Michael', 'Brown', 'AN160')
gr_try.add_student(st5)
st6 = Student('Female', 24, 'Sophia', 'Johnson', 'AN165')
gr_try.add_student(st6)
st7 = Student('Male', 29, 'David', 'Wilson', 'AN170')
gr_try.add_student(st7)
st8 = Student('Female', 27, 'Emma', 'Davis', 'AN175')
gr_try.add_student(st8)
st9 = Student('Male', 31, 'Robert', 'Clark', 'AN180')
gr_try.add_student(st9)
st10 = Student('Female', 23, 'Olivia', 'Miller', 'AN185')
gr_try.add_student(st10)
st11 = Student('Male', 32, 'James', 'Anderson', 'AN190')
try:
    gr_try.add_student(st11)
except AddTenPlusError as errorText:
    print(errorText)