def findLcm(n1, n2):
    a = n1
    b = n2

    while n2 != 0:
        n1, n2 = n2, n1 % n2

    return (a * b) // n1