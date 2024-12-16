initialList = [1, 2, 3, 4, 5, 6, 7]

resultDoubleList = [] 

if len(initialList) == 0:
    resultDoubleList += list(), list()

elif len(initialList) % 2 == 0:
    resultDoubleList.append(initialList[:int(len(initialList) / 2)])
    resultDoubleList.append(initialList[int(len(initialList) / 2):])

else:
    evenLen = len(initialList) + 1

    resultDoubleList.append(initialList[:int(evenLen / 2)])
    resultDoubleList.append(initialList[int(evenLen / 2):])

print(resultDoubleList)