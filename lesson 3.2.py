initialList = [13, 777, 666, 228, 420, 102]

print(f"Before: {initialList}")

initialList.insert(0, initialList[-1])
initialList.pop()

print(f"After: {initialList}")