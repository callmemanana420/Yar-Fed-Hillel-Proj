testList = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

numberToEnd = 0
indexOfNumberToEnd = list()

counter = 0

for index, number in enumerate(testList):
    if number == numberToEnd:
        indexOfNumberToEnd.append(index)
        counter += 1

for i in indexOfNumberToEnd[::-1]:
    testList.pop(i)

for i in range(counter):
    testList.append(numberToEnd)



print(testList)