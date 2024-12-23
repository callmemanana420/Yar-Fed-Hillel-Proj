import string

variableName = "assert_exception"
# variableName = "Enter name of the variable: "
correctSymbols = string.ascii_lowercase + string.digits + "_"
blackListWord = "assert"


isValid = True

for i in variableName:
    if not i in correctSymbols:
        print("Variable have invalid symbols!")
        isValid = False
        break
        

for index, symbol in enumerate(variableName):
    if symbol == "_" and index != (len(variableName) - 1):
        if variableName[index + 1] == "_":
            print("_ after _ issue!")
            isValid = False
            break
    
if variableName[0] in string.digits:
    print("First symbol is number!")
    isValid = False
    
elif blackListWord in variableName and len(blackListWord) == len(variableName):
    print("Black list word!")
    isValid = False


if isValid == True:
    print("Name of variable is corrtct :)")
    


