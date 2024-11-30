import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars, base_word=None):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 1 or not characters:
        return

    password = []
    
    if base_word:
        password.extend(base_word)
        length -= len(base_word)

    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_special_chars:
        password.append(random.choice(string.punctuation))

    password += random.choices(characters, k=length - len(password))
    random.shuffle(password)

    return ''.join(password)
