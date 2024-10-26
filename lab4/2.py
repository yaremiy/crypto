def gcdex(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return (x, y, a)

def inverse_element(a, n):
    x, y, gcd = gcdex(a, n)

    if gcd != 1:
        raise ValueError(f"Оберненого елементу для {a} по модулю {n} не існує")
    else:
        return x % n

a = 5
n = 18
try:
    inverse = inverse_element(a, n)
    print(f"Обернений елемент {a} по модулю {n} дорівнює {inverse}")
    print(f"Перевірка: ({a} * {inverse}) % {n} = {(a * inverse) % n}")
except ValueError as e:
    print(e)