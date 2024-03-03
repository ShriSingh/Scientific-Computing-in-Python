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

def main():
    input_string = input('Enter a string in Camel Case or Pascal Case: ')
    print(f'Snake Case: {convert_to_snake_case(input_string)}')

if __name__ == '__main__':
    main()
