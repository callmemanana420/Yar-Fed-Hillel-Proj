import string

ALPHABET = string.ascii_letters

input_range = input("Enter the range of letters(a-Z): ")


if len(input_range) == 3:
    first_letter = input_range[0]
    second_letter = input_range[2]

    if first_letter in ALPHABET and input_range[1] == "-" and second_letter in ALPHABET:
        first_letter_index = ALPHABET.index(input_range[0])
        second_letter_index = ALPHABET.index(input_range[2])

        if first_letter_index <= second_letter_index:
            print(ALPHABET[first_letter_index:second_letter_index + 1])

        else:
            if second_letter_index == 0:
                print(ALPHABET[first_letter_index::-1])

            else:
                print(ALPHABET[first_letter_index:second_letter_index - 1:-1])
    else:
        print("Ivalid input")
else:
    print("Invalid lenth of input!")