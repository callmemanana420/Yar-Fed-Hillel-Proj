keepWorking = "yes"

while keepWorking == "yes":

    firstNumber = int(input("Enter first number: "))
    operator = input("Enter operator(+, -, *, /): ")
    secondNumber = int(input("Enter second number: "))

    if operator == "/" and secondNumber == 0:
        print("Division by zero!")
    else:
        match operator:
            case "+":
                print(f"Answer is: {firstNumber + secondNumber}")
            case "-":
                print(f"Answer is: {firstNumber - secondNumber}")
            case "*":
                print(f"Answer is: {firstNumber * secondNumber}")
            case "/":
                print(f"Answer is: {firstNumber / secondNumber}")
            case _:
                print("Enter correct operator!")

    while True:
        print("\nDo you want keep working with calculator?")
        keepWorking = input("Enter your answer(yes, no): ")
        if keepWorking == "yes":
            print("Starting a new operation...\n")
            break
        elif keepWorking == "no":
            print("Close the program...")
            break
        else:
            print("\nWrong answer! Enter 'yes' or 'no'!")