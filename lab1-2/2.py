def encrypt_gronsfeld_custom(plaintext, key):
    """Шифрування тексту за шифром Гронсфельда з заданим алфавітом."""
    alphabet = 'АБВГДЕЖЗИК'  # Алфавіт за зразком
    key_numbers = [int(k) for k in key]  # Перетворюємо ключ у список чисел
    ciphertext = []

    for i, char in enumerate(plaintext.upper()):
        if char in alphabet:
            # Отримуємо індекс символу в алфавіті
            char_index = alphabet.index(char)
            # Використовуємо ключ для зміщення
            shift = key_numbers[i % len(key_numbers)]
            # Обчислюємо новий індекс символу
            new_index = (char_index + shift) % len(alphabet)
            # Додаємо зашифрований символ до результату
            ciphertext.append(alphabet[new_index])
        else:
            # Якщо символ не в алфавіті, додаємо його без змін
            ciphertext.append(char)

    return ''.join(ciphertext)

def decrypt_gronsfeld_custom(ciphertext, key):
    """Розшифрування тексту за шифром Гронсфельда з заданим алфавітом."""
    alphabet = 'АБВГДЕЖЗИК'  # Алфавіт за зразком
    key_numbers = [int(k) for k in key]  # Перетворюємо ключ у список чисел
    plaintext = []

    for i, char in enumerate(ciphertext.upper()):
        if char in alphabet:
            # Отримуємо індекс символу в алфавіті
            char_index = alphabet.index(char)
            # Використовуємо ключ для зворотного зміщення
            shift = key_numbers[i % len(key_numbers)]
            # Обчислюємо новий індекс символу
            new_index = (char_index - shift) % len(alphabet)
            # Додаємо розшифрований символ до результату
            plaintext.append(alphabet[new_index])
        else:
            # Якщо символ не в алфавіті, додаємо його без змін
            plaintext.append(char)

    return ''.join(plaintext)

# Приклад використання
if __name__ == "__main__":
    plaintext = "ЗАДВИЖКА"
    key = "513"

    encrypted = encrypt_gronsfeld_custom(plaintext, key)
    print(f"Зашифрований текст: {encrypted}")

    decrypted = decrypt_gronsfeld_custom(encrypted, key)
    print(f"Розшифрований текст: {decrypted}")
