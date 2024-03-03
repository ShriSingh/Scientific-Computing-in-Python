'''
Making a Case Converter
    - Converts a string formatted in Camel Case(or Pascal Case) 
    to Snake Case
    - Shows two different ways of conversion:
        1. Normal version
        2. List comprehension version
'''
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []

    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)

    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string

def convert_to_snake_case_2(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()        # --> place '_' & concatenate a lowercase of the letter if it's in uppercase
        else char                                   # --> Otherwise put a the default letter
        for char in pascal_or_camel_cased_string    # --> For every character in the string
    ]

    return ''.join(snake_cased_char_list).strip('_')    # Doing a combined operation of joining the list and stripping any dangling underscores

def main():
    input_string = input('Enter a string in Camel Case or Pascal Case: ')
    print(f'Snake Case using normal version: {convert_to_snake_case(input_string)}')
    print(f'Snake Case using list comprehension: {convert_to_snake_case_2(input_string)}')

if __name__ == '__main__':
    main()
