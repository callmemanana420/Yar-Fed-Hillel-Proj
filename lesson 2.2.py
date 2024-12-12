usersInput = int(input('Enter five numbers: '))#13553

number1 = usersInput // 10000
number2 = usersInput // 1000 % 10
number3 = usersInput // 100 % 10
number4 = usersInput // 10 % 10
number5 = usersInput % 10

print(number5, number4, number3, number2, number1, sep='')