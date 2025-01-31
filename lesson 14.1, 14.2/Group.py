from AddTenPlusError import AddTenPlusError

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
    def add_student(self, student):
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
    def find_student(self, comparison_string): #14.2
        comparison_string = str(comparison_string)
        for student in self.group:
            if comparison_string in student.__dict__.values():
                # return f"{student.first_name} {student.last_name}" # Это вроде неверное решение
                # print(f"{student.first_name} {student.last_name}") # Може еще так делать. Но я не уверен, поэтому оставлю так.
                return student
        return None
    def __str__(self):
        all_students = ", ".join([f"{i.first_name} {i.last_name}" for i in self.group])
        return f'Number: {self.number}\nStudents: {all_students}'
        # return f'{len(self.group)}'


# from Student import Student
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
# assert gr.find_student('Jobs2') is None
# print(gr.find_student('Jobs')) # 'Steve Jobs'
# gr.delete_student('Taylor')
# # print(gr) # Only one student
