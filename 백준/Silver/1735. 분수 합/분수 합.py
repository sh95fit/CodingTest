import math

A, B = map(int, input().split())
C, D = map(int, input().split())

numerator = A*D + B*C
denominator = B*D

gcd = math.gcd(numerator, denominator)

numerator //= gcd
denominator //= gcd

print(numerator, denominator)