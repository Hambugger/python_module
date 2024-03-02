#A Function divisible by 10

def divisible_by_ten(num):
    remainder = num % 10
    if remainder == 0:
        return True
    else:
        return False
print(divisible_by_ten(1000))
print(divisible_by_ten(5))


def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
print(large_power(10, 3))
print(large_power(10, 5))