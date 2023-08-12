def is_power(a, b):
    print(a, b, a % b, a // b)
    if a < b:
        return False
    if a == b:
        return True
    if a % b == 0:
        return is_power(a // b, b)
    return False


print(is_power(8, 2))

