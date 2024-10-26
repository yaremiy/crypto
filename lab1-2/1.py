import re

#Видаляєм небажані символи з тексту
def sanitize_text(text):
    return ''.join(filter(str.isalnum, text))

#Створення матриці з тексту
def create_matrix(text, num_rows, num_cols):
    matrix = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]
    sanitized_text = sanitize_text(text)

    for index, char in enumerate(sanitized_text):
        row = index // num_cols
        col = index % num_cols
        if row < num_rows:  
            matrix[row][col] = char

    return matrix

#Шифрування тексту на основі ключів для рядків і колонок
def encrypt(text, row_key, col_key):
    num_rows = len(row_key)
    num_cols = len(col_key)

    matrix = create_matrix(text, num_rows, num_cols)

    sorted_col_indices = sorted(range(len(col_key)), key=lambda i: col_key[i])
    sorted_row_indices = sorted(range(len(row_key)), key=lambda i: row_key[i])

    encrypted_text = []
    for col in sorted_col_indices:
        for row in sorted_row_indices:
            encrypted_text.append(matrix[row][col])

    return ''.join(encrypted_text)
#Позиції пробілів
def get_space_positions(text):
    return [i for i, char in enumerate(text) if char == ' ']

#Розшифрування
def decrypt(encrypted_text, row_key, col_key, space_positions):
    num_rows = len(row_key)
    num_cols = len(col_key)

    matrix = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]

    text_index = 0
    sorted_col_indices = sorted(range(len(col_key)), key=lambda i: col_key[i])
    sorted_row_indices = sorted(range(len(row_key)), key=lambda i: row_key[i])

    for col in sorted_col_indices:
        for row in sorted_row_indices:
            if text_index < len(encrypted_text):
                matrix[row][col] = encrypted_text[text_index]
                text_index += 1

    decrypted_text = []
    for row in range(num_rows):
        for col in range(num_cols):
            decrypted_text.append(matrix[row][col])

    #Додаємо пробіли
    decrypted_text = ''.join(decrypted_text).strip()
    decrypted_list = list(decrypted_text) 

    for pos in space_positions:
        decrypted_list.insert(pos, ' ')

    return ''.join(decrypted_list).strip()

original_text = "програмне забезпечення"
column_key = "крипто"
row_key = "шифр"

print(f"Вихідний текст: {original_text}")

#Зберігаємо позиції пробілів з вихідного тексту
space_positions = get_space_positions(original_text)

encrypted_text = encrypt(original_text, row_key, column_key)
print(f"Зашифрований текст: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, row_key, column_key, space_positions)
print(f"Розшифрований текст: {decrypted_text}")