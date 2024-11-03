import random

def is_prime(n, k):
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
n = 19
a = is_prime(n, 50)
print(f"Число {n} просте? {a}")