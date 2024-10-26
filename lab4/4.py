def gcdex(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return (x, y, a)

def inverse_element_2(a, p):
    if a % p == 0:
        raise ValueError(f"Оберненого елементу для {a} по модулю {p} не існує")
    return pow(a, p - 2, p)  # мала теореми Ферма

a = 5
p = 18
try:
    inverse_2 = inverse_element_2(a, p)
    print(f"Обернений елемент {a} по модулю {p} дорівнює {inverse_2}")
    print(f"Перевірка: ({a} * {inverse_2}) % {p} = {(a * inverse_2) % p}")
except ValueError as e:
    print(e)

