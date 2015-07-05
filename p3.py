def kol(n):
    a = n % 2
    if a == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    print n
    if n != 1:
        kol(n)

n = 13.0
kol(n)

