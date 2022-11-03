def xpto(n1, n2):
    while n1 != n2:
        if (n1 < n2):
            n2 = n2 - n1
        else:
            n1 -= n2
    return n1
print(xpto(50, 5))

