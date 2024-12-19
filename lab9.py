import random

def is_prime_miller_rabin(n, k):
    if n < 2 or n % 2 == 0:
        return 0
    d = n - 1
    r = 0
    while d % 2 == 0:
        d >>= 1
        r += 1
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False # бо 1
            if x == n - 1:
                continue
        return False  # складне
    return True  # просте

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime_miller_rabin(num, 5):
            return num

def generate_generator(p):
    phi = p - 1
    while True:
        g = random.randint(2, p - 1)
        if pow(g, 2, p) != 1 and pow(g, phi // 2, p) != 1:
            return g

def text_to_numbers(text):
    return [ord(char) for char in text]

def numbers_to_text(numbers):
    return ''.join([chr(num) for num in numbers])

def generate_keypair(bits):
    p = generate_prime(bits)
    g = generate_generator(p)
    x = random.randint(1, p - 1)
    y = pow(g, x, p)

    public_key = (p, g, y)
    private_key = (p, x)

    return public_key, private_key

def elgamal_encrypt(message, p, g, y):
    m_numbers = text_to_numbers(message)
    k = random.randint(1, p - 2)
    c1 = pow(g, k, p)
    c2 = [(m * pow(y, k, p)) % p for m in m_numbers]
    return c1, c2

def elgamal_decrypt(ciphertext, p, x):
    c1, c2 = ciphertext
    s = pow(c1, x, p)
    s_inv = pow(s, -1, p)
    m_numbers = [(c * s_inv) % p for c in c2]
    return numbers_to_text(m_numbers)

(p, g, y), (_, x) = generate_keypair(256)

message_to_encrypt = input("Введіть рядок для шифрування: ")
ciphertext = elgamal_encrypt(message_to_encrypt, p, g, y)
decrypted_message = elgamal_decrypt(ciphertext, p, x)

print(f"Зашифроване повідомлення: {ciphertext}")
print(f"Розшифроване повідомлення: {decrypted_message}")