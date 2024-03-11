# Learning how to work with numbers & strings by implementing Luhn's Algorithm

def verify_card_number(card_number):
    '''
    Implementing a Luhn Algorithm
        - Go thru the number from right to left and double every second digit
            - If product is greater than 9, then add the digits together
            (E.g. In 7 9 9 2, 9 * 2 = 18 --> 18 > 9 --> 1 + 8 = 9)
        - If the sum of all the digits is a multiple of 10, then the number is valid
    '''
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    
    total = sum_of_odd_digits + sum_of_even_digits

    sum_check = total % 10

    return sum_check == 0

def main():
    """
    Main function to run the program
    """
    # Try numbers: 4111-1111-4555-1142, 4111-1111-1111-1111, 1234-5678-9012-3456
    card_number = input("Enter your card number('XXXX-XXXX-XXXX-XXXX'): ")
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

if __name__ == '__main__':
    main()