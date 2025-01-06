def second_index(text, some_str): 
    indexOfFirstLetter = text.find(some_str)
    indexOfSecondLetter = text.find(some_str, indexOfFirstLetter + 1)

    if indexOfSecondLetter == -1:
        return None

    else:
        return indexOfSecondLetter

assert second_index("sims", "s") == 3, 'Test1' 
assert second_index("find the river", "e") == 12, 'Test2' 
assert second_index("hi", "h") is None, 'Test3' 
assert second_index("Hello, hello", "lo") == 10, 'Test4' 
print('ОК')
