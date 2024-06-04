from itertools import combinations

from math import gcd

def lcm(a, b):

    return a * b // gcd(a, b)


def lcm_of_three(a, b, c):

    return lcm(lcm(a, b), c)

def at_least_mostly_multiple(nums):

    min_lcm = float('inf')

    for comb in combinations(nums, 3):

        current_lcm = lcm_of_three(*comb)

        if current_lcm < min_lcm:

            min_lcm = current_lcm

    return min_lcm

nums = list(map(int, input().split()))

print(at_least_mostly_multiple(nums))

