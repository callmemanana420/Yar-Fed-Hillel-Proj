from Student import Student
from Group import Group
from AddTenPlusError import AddTenPlusError

def main():	
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

	#14.2
	gr = Group('PD1')
	gr.add_student(st1)
	gr.add_student(st2)
	print(gr)
	assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
	assert gr.find_student('Jobs2') is None
	gr.find_student('Jobs') # 'Steve Jobs'




if __name__ == '__main__':
    main()