def power(x, n):
    result = 1
    base = x
    exponent = n
    if n < 0:
        base = 1 / x
        exponent = -n
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result


def power2(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half
    return x * power(x, n - 1)


x = power2(2, -4)
print(x)
