import random

def is_prime(n, k=40):
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

def generate_large_prime(bits=1024):
    while True:
        number = random.getrandbits(bits) | (1 << (bits - 1)) | 1  
        if is_prime(number):
            return number


def extended_gcd(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (a, x, y)


def generate_keys(bits=1024):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    while p == q:  
        q = generate_large_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  
    gcd, _, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("e та φ(n) мають бути взаємно простими!")
    _, d, _ = extended_gcd(e, phi)
    d = d % phi  
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key


def encrypt(plaintext, public_key):
    e, n = public_key
    return pow(plaintext, e, n)

def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

public_key, private_key = generate_keys()

message = 100  
ciphertext = encrypt(message, public_key)
decrypted_message = decrypt(ciphertext, private_key)

# print("Публічний ключ:", public_key)
# print("Приватний ключ:", private_key)
print("Оригінальне повідомлення:", message)
print("Зашифроване повідомлення:", ciphertext)
print("Розшифроване повідомлення", decrypted_message)
