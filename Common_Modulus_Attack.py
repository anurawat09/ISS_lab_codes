#!/usr/bin/env python3

from math import gcd

def long_to_bytes(n):
    byte_length = (n.bit_length() + 7) // 8
    return n.to_bytes(byte_length, 'big')


def inverse(a, m):
    return pow(a, -1, m)


def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return x, y


def common_modulus_attack(c1, c2, e1, e2, n):
    if gcd(e1, e2) != 1:
        raise ValueError("e1 and e2 must be coprime")

    s1, s2 = extended_gcd(e1, e2)

    if s1 < 0:
        c1 = inverse(c1, n)
        s1 = -s1
    if s2 < 0:
        c2 = inverse(c2, n)
        s2 = -s2

    m = (pow(c1, s1, n) * pow(c2, s2, n)) % n
    return long_to_bytes(m)


if __name__ == "__main__":
    
    n = 2534669 
    e1 = 17
    e2 = 13
    m = 42      

    
    c1 = pow(m, e1, n)
    c2 = pow(m, e2, n)

    print(f"Original message: {m}")
    print(f"Ciphertext c1: {c1}")
    print(f"Ciphertext c2: {c2}")

    
    recovered_bytes = common_modulus_attack(c1, c2, e1, e2, n)
    recovered_int = int.from_bytes(recovered_bytes, byteorder='big')

    print(f"\nRecovered message (bytes): {recovered_bytes}")
    print(f"Recovered message (int): {recovered_int}")
