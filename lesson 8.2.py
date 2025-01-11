import string

LETTERS = string.ascii_letters
NUMBERS = [str(number) for number in range(10)]


def is_palindrome(text):
    clean_text = str()

    for letter in text:
        if letter in LETTERS or letter in NUMBERS:
            clean_text += letter

    clean_text = clean_text.lower()

    clean_text_reverse = clean_text[::-1]

    if clean_text == clean_text_reverse:
        return True
    else:
        return False
    

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1' 
assert is_palindrome('0P') == False, 'Test2' 
assert is_palindrome('a.') == True, 'Test3' 
assert is_palindrome('aurora') == False, 'Test4' 
print("ОК")
