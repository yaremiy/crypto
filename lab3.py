


# Константи для таблиць DES
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

EBox = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# SBox таблиці
SBox =[
		# S1
		[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
		 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
		 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
		 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

		# S2
		[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
		 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
		 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
		 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

		# S3
		[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
		 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
		 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
		 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

		# S4
		[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
		 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
		 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
		 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

		# S5
		[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
		 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
		 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
		 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

		# S6
		[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
		 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
		 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
		 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

		# S7
		[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
		 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
		 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
		 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

		# S8
		[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
		 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
		 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
		 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
	]


F_PBox = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
          2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

key_PBox = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

def xor(left, right):
    return [l ^ r for l, r in zip(left, right)]

def E_box(right):
    return [right[i - 1] for i in EBox]

def sboxlookup(sinput, x):
    row = int(f"{sinput[0]}{sinput[5]}", 2)
    column = int(''.join(map(str, sinput[1:5])), 2)
    element = SBox[x - 1][16 * row + column]
    return [int(bit) for bit in f"{element:04b}"]

def sbox(sboxin):
    return sum([sboxlookup(sboxin[i:i+6], idx+1) for idx, i in enumerate(range(0, 48, 6))], [])

def f_permute(data):
    return [data[i - 1] for i in F_PBox]

def f_function(right, rkey):
    return f_permute(sbox(xor(E_box(right), rkey)))

def round(data, rkey):
    left, right = data[:32], data[32:]
    return right + xor(left, f_function(right, rkey))

def permutation(data, perm_type):
    table = IP if perm_type == 0 else FP
    return [data[i - 1] for i in table]

def userinput():
    keyinp = input("Введіть біти ключа (56 біт) (розділені пробілом): ").strip().split()
    datainp = input("Введіть біти даних (64 біти) для шифрування (розділені пробілом): ").strip().split()
    
    if len(datainp) == 64 and len(keyinp) == 56:
        print("Дані та ключ успішно завантажені")
    else:
        while len(datainp) != 64:
            print(f"Довжина введених даних: {len(datainp)}")
            datainp = input("Помилка введення. Введіть дані (64 біти), розділені пробілом: ").strip().split()
        print("Дані успішно завантажені")
        
        while len(keyinp) != 56:
            print(f"Довжина введеного ключа: {len(keyinp)}")
            keyinp = input("Помилка введення. Введіть ключ (56 біт), розділений пробілом: ").strip().split()
        print("Ключ успішно завантажено")
    
    return list(map(int, keyinp)), list(map(int, datainp))

def keyshift(toshift, n):
    shift = 1 if n in [1, 2, 9, 16] else 2
    return toshift[shift:] + toshift[:shift]

def keypermute(key16):
    return [[key[i - 1] for i in key_PBox] for key in key16]

def keyschedule(key):
    left, right = key[:28], key[28:]
    key16 = [keyshift(left, i+1) + keyshift(right, i+1) for i in range(16)]
    return keypermute(key16)

def encrypt(data, key16):
    data = permutation(data, 0)
    for i in range(16):
        data = round(data, key16[i])
    return permutation(data[32:] + data[:32], 1)

def decrypt(data, key16):
    data = permutation(data, 0)
    for i in range(16):
        data = round(data, key16[15 - i])
    return permutation(data[32:] + data[:32], 1)

def compare_messages(original, decrypted):
    if original == decrypted:
        print("Повідомлення успішно розшифровано: оригінальне та розшифроване співпадають!")
    else:
        print("Помилка розшифрування: оригінальне та розшифроване повідомлення не співпадають.")


key, data = userinput()
key16 = keyschedule(key)

# Шифрування
encrypted_data = encrypt(data, key16)
print("Зашифроване повідомлення:", encrypted_data)

# Розшифрування
decrypted_data = decrypt(encrypted_data, key16)
print("Розшифроване повідомлення:", decrypted_data)

# Порівняння результатів
compare_messages(data, decrypted_data)

