def GCD(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a = a - b
        else:
            b = b - a
    return a + b


def GCD2(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b


def GCD3(a, b):
    if a == 0 or b == 0:
        return a + b
    if a >= b:
        return GCD3(a % b, b)
    else:
        return GCD3(a, b % a)
