import string

CORRECT_SYMBOLS = string.ascii_letters

inputWithCorrectStmbols = ["#"]

usersInput = input("Enter text for hashtag: ").title()

if len(usersInput) != 0:
    for i in usersInput:
        if i in CORRECT_SYMBOLS:
            inputWithCorrectStmbols.append(i)
    
    if len(inputWithCorrectStmbols) == 1:
        print('Your hashtag is void')    
    else:
        inputWithCorrectStmbols = ''.join(inputWithCorrectStmbols)      
        print(inputWithCorrectStmbols)

else:
    print('Your hashtag is void')
