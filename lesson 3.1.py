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