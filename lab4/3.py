def phi(m):
    result = m
    p = 2

    while p * p <= m:
        if m % p == 0:
            result -= result // p
            while m % p == 0:
                m //= p
        p += 1

    if m > 1:
        result -= result // m

    return result

m = 11
result = phi(m)
print(f"Значення функції Ейлера φ({m}) = {result}")
