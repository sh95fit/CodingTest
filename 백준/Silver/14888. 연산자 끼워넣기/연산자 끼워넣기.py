from itertools import permutations

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if a < 0:
            return -(-a // b)
        return a // b

def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    
    operators = ['+'] * add + ['-'] * sub + ['*'] * mul + ['/'] * div
    max_result = -int(1e9)
    min_result = int(1e9)
    
    for perm in set(permutations(operators)):
        result = numbers[0]
        for i in range(n - 1):
            result = calculate(result, numbers[i + 1], perm[i])
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    
    print(max_result)
    print(min_result)

solve()