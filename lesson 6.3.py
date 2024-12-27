input_numbers = input("Enter a number: ")



if input_numbers.isdigit():

    input_numbers = int(input_numbers)

    while input_numbers > 9:
        final_result = 1

        for num in str(input_numbers):
            final_result *= int(num)

        input_numbers = final_result

    print(final_result)
else:
    print("Input is not a number")
