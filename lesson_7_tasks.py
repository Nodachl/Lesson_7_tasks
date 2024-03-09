# 1
def get_power(base, exponent):
    if exponent == 0:
        return 1
    return base * get_power(base, exponent - 1)

print(get_power(2, 6))

# 2
def print_stars(n):
    if n == 0:
        return
    else:
        print('*', end='')
        print_stars(n - 1)

print_stars(5)

# 3
def calc_sum(a, b):
    if a > b:
        return 0
    else:
        return a + calc_sum(a + 1, b)

print(calc_sum(2, 5))