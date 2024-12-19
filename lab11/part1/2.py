def gcdex(a, b):
    x_0, x_1 = 1, 0
    y_0, y_1 = 0, 1
    d_0, d_1 = a, b
    while d_1 != 0:
        q = d_0 // d_1
        d_0, d_1 = d_1, d_0 - d_1 * q
        x_0, x_1 = x_1, x_0 - q * x_1
        y_0, y_1 = y_1, y_0 - q * y_1

    return d_0, x_0, y_0

def inverse_element(a, n):
    g, x, _ = gcdex(a, n)
    if g == 1:
        return x % n
    else:
        raise ValueError("Оберненого елемента не існує! Числа не є взаємно прості!")

def add_points(p, q, a, p_field):
    if p == (None, None):
        return q
    if q == (None, None):
        return p

    if p[0] == q[0] and p[1] != q[1]:
        return (None, None)  

    if p == q:
        temp = inverse_element(2 * p[1], p_field)
        m = (3 * pow(p[0], 2) + a) * temp % p_field
    else:
        temp = inverse_element(q[0] - p[0], p_field)
        m = (q[1] - p[1]) * temp % p_field

    x_r = (pow(m, 2) - p[0] - q[0]) % p_field
    y_r = (m * (p[0] - x_r) - p[1]) % p_field

    return (x_r, y_r)

def multiply_point(base_point, scalar, a, p_field):
    result = (None, None) 
    temp = base_point

    for bit in bin(scalar)[2:]:
        if bit == '1':
            result = add_points(result, temp, a, p_field)
        temp = add_points(temp, temp, a, p_field)

    return result

def find_order(base_point, a, p):
    order = 1
    result = base_point
    print(f"Точка {order} - {result}")
    while result != (None, None):  
        result = add_points(result, base_point, a, p)
        order += 1
        print(f"Точка {order} - {result}")
    return order

a = 1
b = 1
mod_p = 23
point = (17, 20)

# Перевірка належності точки кривій
if (point[1] ** 2) % mod_p == (point[0] ** 3 + a * point[0] + b) % mod_p:
    order = find_order(point, a, mod_p)
    print(f"Порядок точки {point} еліптичної кривої y^2 = x^3 + {a}x + {b} (mod {mod_p}): {order}")
else:
    print("Точка не належить еліптичній кривій!")