import random

def is_prime_miller_rabin(n, k=5):
    if n <= 2:
        return n == 2
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


print(is_prime_miller_rabin(97))  # True
print(is_prime_miller_rabin(91))  # False
