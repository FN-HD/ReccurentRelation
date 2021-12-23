
# return a^{-1} mod b
def modinv(a, b):
    p = b
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    x %= p
    if x < 0:
        x += p
    return x