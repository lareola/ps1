
def obrposled(x,a,b):
    l = len(x)
    for j in range(l):
        if x[j] < a:
            x[j] = a
        if x[j] > b:
            x[j] = b
    print x

x = [1, 2, 3, 4, 5]
obrposled(x, 2, 4)