# Learning String manipulation by Building a Cipher

def caesar(message, offset):
    '''
    Writing a Caesar Cipher
    - Shifts each letter with the same given offset
    : param message: The message to be encrypted
    : param offset: The number of positions to shift each letter
    : return: plain text & encrypted message
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return 'plain text:', message + '\nencrypted text:', encrypted_text


def vigenere(message, key, direction=1):
    '''
    Writing a Vigenere Cipher
    - Uses a keyword to shift each letter
    : param message: The message to be encrypted
    : param key: The keyword to be used for encryption
    : param direction: The direction of the shift (1 for encryption, -1 for decryption)
    : return: The encrypted/decrypted message
    '''
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + (offset * direction)) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

def encrypt(message, key):
    """Encrypting function"""
    return vigenere(message, key)

def decrypt(message, key):
    """Decrypting function"""
    return vigenere(message, key, -1)
