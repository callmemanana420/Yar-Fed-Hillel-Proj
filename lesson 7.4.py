
def common_elements():
    initialList = range(100)

    listMultiplesThree = set([number for number in initialList if number % 3 == 0])
    listMultiplesFive = set([number for number in initialList if number % 5 == 0])

    finalResultList = listMultiplesThree.intersection(listMultiplesFive)

    return finalResultList


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
 