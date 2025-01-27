def is_even(number):
    # first = number / 2
    # second = int(first)
    # third = first - second
    # return third == 0
    
    valid_end = ["0", "2", "4", "6", "8"]
    last_str_number = str(number)[-1]

    return last_str_number in valid_end

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

print("ok")
