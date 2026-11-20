import math

''' Check if a number is prime '''
def is_prime_number(x):
    if x < 2:  # 0, 1 은 소수가 아님
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(is_prime_number(4)) # False
print(is_prime_number(7)) # True

assert not is_prime_number(1)
assert is_prime_number(2)
