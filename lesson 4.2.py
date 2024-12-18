#1
testList = [0, 1, 7, 2, 4, 8]

lenOfTestList = len(testList)

finalResult = 0

for i in testList[::2]:
    finalResult += i

finalResult = finalResult * testList[-1]

print(finalResult)


# #2
# testList = [0, 1, 7, 2, 4, 8]

# lenOfTestList = len(testList)

# finalResult = 0

# if len(testList) > 1:

#     if len(testList) % 2 == 0:
#         for i in testList[::2]:
#             finalResult += i
#     else:
#         for i in testList[:-1:2]:
#             finalResult += i

#     finalResult = finalResult * testList[-1]

# elif len(testList) == 1:
#     finalResult = testList[0]

# print(finalResult)