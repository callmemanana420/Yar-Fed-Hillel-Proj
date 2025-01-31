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
    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
    def __str__(self):
        all_students = ", ".join([f"{i.first_name} {i.last_name}" for i in self.group])
        return f'Number: {self.number}\nStudents: {all_students}'
        # return f'{len(self.group)}'
