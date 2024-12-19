def rotate_left(value, bits):
    return ((value << bits) | (value >> (32 - bits))) & 0xFFFFFFFF

def serialize_words(word_list):
    return b''.join(word.to_bytes(4, 'big') for word in word_list)

def sha1_hash(input_message):
    initial_length = len(input_message)
    input_message += b'\x80'
    padding_length = (56 - (initial_length + 1) % 64) % 64
    input_message += b'\x00' * padding_length
    input_message += (initial_length * 8).to_bytes(8, 'big')

    h0, h1, h2, h3, h4 = (0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0)

    for offset in range(0, len(input_message), 64):
        block = input_message[offset:offset + 64]
        w = [int.from_bytes(block[i:i + 4], 'big') for i in range(0, 64, 4)]
        for i in range(16, 80):
            w.append(rotate_left(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1))

        a, b, c, d, e = h0, h1, h2, h3, h4

        for i in range(80):
            if i < 20:
                func, k = (b & c) | (~b & d), 0x5A827999
            elif i < 40:
                func, k = b ^ c ^ d, 0x6ED9EBA1
            elif i < 60:
                func, k = (b & c) | (b & d) | (c & d), 0x8F1BBCDC
            else:
                func, k = b ^ c ^ d, 0xCA62C1D6

            temp = (rotate_left(a, 5) + func + e + k + w[i]) & 0xFFFFFFFF
            e, d, c, b, a = d, c, rotate_left(b, 30), a, temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    return serialize_words([h0, h1, h2, h3, h4])

user_input = input("Введіт текст, який потріюно захешувати: ").encode("UTF-8")
hashed_result = sha1_hash(user_input).hex()
print(f'Хеш повідомлення: {hashed_result}')