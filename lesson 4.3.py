import random

minLengthOfList = 3
maxLengthOfList = 10
lengthOfList = random.randint(minLengthOfList, maxLengthOfList)

listWithRandomNumber = list()

finalList = list()



for _ in range(lengthOfList):
    listWithRandomNumber.append(random.randint(0, 9))

print(f"First list with random numbers: {listWithRandomNumber}")

indexes = [0, 2, -2]

for i in indexes:
    finalList.append(listWithRandomNumber[i])

print(f"Final list: {finalList}")