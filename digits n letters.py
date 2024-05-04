def count_digits_and_letters(input_string):
    num_digits = 0
    num_letters = 0
    for char in input_string:
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():
            num_letters += 1
    return num_digits, num_letters

def main():
    input_string = input("Enter a string: ")
    digit_count, letter_count = count_digits_and_letters(input_string)
    print("Number of digits:", digit_count)
    print("Number of letters:", letter_count)

if __name__ == "__main__":
    main()
