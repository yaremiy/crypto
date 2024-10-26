def gcdex(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)

a = 612
b = 342
x, y, d = gcdex(a, b)
print(f"НСД({a}, {b}) = {d}")
print(f"x = {x}; y = {y}")
print(f"Перевірка: {a}*({x}) + {b}*({y}) = {d}")