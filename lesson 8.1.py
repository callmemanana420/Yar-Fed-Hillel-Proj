def add_one(some_list):
    plus_number = 1

    some_list_items_into_str = [str(i) for i in some_list]
    some_list_str = ''.join(some_list_items_into_str)
    some_list_int = int(some_list_str)
    some_list_int += plus_number
    
    final_result = [int(i) for i in str(some_list_int)]

    return final_result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1' 
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2' 
assert add_one([0]) == [1], 'Test3' 
assert add_one([9]) == [1, 0], 'Test4' 
print("ОК")
