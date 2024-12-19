import random

def gcdex(a, b):
    x_0, x_1 = 1, 0
    y_0, y_1 = 0, 1
    d_0, d_1 = a, b
    while d_1 != 0:
        q = d_0 // d_1
        d_0, d_1 = d_1, d_0 - d_1 *q
        x_0, x_1 = x_1, x_0 - q * x_1
        y_0, y_1 = y_1, y_0 - q * y_1

    return d_0, x_0, y_0

def inverse_element(a, n):
    g, x, y = gcdex(a, n)
    if g == 1:
        return x % n
    else:
        raise ValueError("Оберненого елемента не існує! Числа не є взаємно прості!")
    
def find_generator(a, b, p):
    x, y = random.randint(1, p - 1), random.randint(1, p - 1)
    while (y ** 2) % p != (x ** 3 + a * x + b) % p:
        x, y = random.randint(0, p - 1), random.randint(0, p - 1)

    return (x, y)
    
    
def add_points(p, q, a, mod_p):
    if p[0] != q[0] or p[1] != q[1]:
        m = (q[1] - p[1]) * inverse_element(q[0] - p[0], mod_p)
    else:
        m = (3 * pow(p[0], 2) + a) * inverse_element(2 * p[1], mod_p)
    x_r = (pow(m, 2) - p[0] - q[0]) % mod_p
    y_r = (m * (p[0] - x_r) - p[1]) % mod_p

    return x_r, y_r

def multiply_point(p, scalar, a, mod_p):
    result = p
    for bit in bin(scalar)[3:]:
        result = add_points(result, result, a, mod_p)
        if bit == '1':
            result = add_points(result, p, a, mod_p)

    return result

def find_order(base_point, a, mod_p):
    order = 1
    result = base_point
    while result[0] != base_point[0] or order == 1:
        order += 1
        result = multiply_point(base_point, order, a, mod_p)
    
    return order + 1

def generate_keypair(g, a, p):
    private_key = random.randint(1, find_order(g, a, p) - 1)
    public_key = multiply_point(g, private_key, a, p)

    return private_key, public_key

def encrypt(message, public_key, g, a, p):
    k = random.randint(1, find_order(g, a, p) - 2)
    c1 = multiply_point(g, k, a, p)
    t = multiply_point(public_key, k, a, p)
    c2 = add_points(message, t, a, p)

    return c1, c2

def decrypt(c1, c2, private_key, a, p):
    s = multiply_point(c1, private_key, a, p)
    s_inverse = (s[0], (-s[1]) % p)
    message = add_points(c2, s_inverse, a, p)
    
    return message


a = 1
b = 1
mod_p = 23
message = (12, 19)
g = find_generator(a, b, mod_p)
private_key, public_key = generate_keypair(g, a, mod_p)

encrypted_message = encrypt(message, public_key, g, a, mod_p)
decrypted_message = decrypt(encrypted_message[0], encrypted_message[1], private_key, a, mod_p)

print("Повідомлення:", message)
print("Генератор:", g)
print("Публічний ключ:", public_key)
print("Приватний ключ:", private_key)
print("Зашифроване повідомлення:", encrypted_message)
print("Розшифроване повідомлення:", decrypted_message)