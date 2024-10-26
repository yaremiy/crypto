import random

# Таблиця гомофонічної заміни
homophonic_table = {
    'А': [17, 31, 48],
    'Б': [23, 44, 63],
    'В': [14, 89, 42],
    'Г': [55, 52, 11],
    'Д': [37, 88, 25],
    'Е': [97, 51, 15],
    'Ж': [47, 67, 33],
    'З': [76, 19, 59],
    'И': [27, 64, 73],
    'К': [77, 38, 45]
}

# Функція для шифрування
def encrypt_homophonic(plaintext):
    ciphertext = []
    for char in plaintext.upper():
        if char in homophonic_table:
            # Вибираємо випадковий варіант із можливих
            cipher_symbol = random.choice(homophonic_table[char])
            ciphertext.append(str(cipher_symbol))
        else:
            # Якщо символ не в таблиці, додаємо його без змін
            ciphertext.append(char)
    return ''.join(ciphertext)

# Функція для розшифрування
def decrypt_homophonic(ciphertext):
    reverse_table = {str(val): key for key, values in homophonic_table.items() for val in values}
    plaintext = []
    i = 0
    while i < len(ciphertext):
        # Беремо двозначне число як зашифрований символ
        cipher_symbol = ciphertext[i:i+2]
        if cipher_symbol in reverse_table:
            plaintext.append(reverse_table[cipher_symbol])
            i += 2  # Переходимо до наступного символу
        else:
            plaintext.append(ciphertext[i])
            i += 1
    return ''.join(plaintext)

# Приклад
plaintext = "ЖАДАЖА"
print(f"Вихідний текст: {plaintext}")

# Шифрування
encrypted_text = encrypt_homophonic(plaintext)
print(f"Зашифрований текст: {encrypted_text}")

# Розшифрування
decrypted_text = decrypt_homophonic(encrypted_text)
print(f"Розшифрований текст: {decrypted_text}")
