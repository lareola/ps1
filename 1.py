__author__ = 'anuta'
def kymylsum(x):
    a = len(x)
    y = [0] + x
    for j in range(1, a+1):
        y[j] = y[j] + y[j-1]

    print y

x=[0, 2 ,4]
kymylsum(x)


