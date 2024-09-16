def calculate_custom_product(A, B):
    sum_A = sum(int(digit) for digit in A)
    sum_B = sum(int(digit) for digit in B) 
   
    result = sum_A * sum_B

    return result

import sys

input = sys.stdin.read
data = input().strip()
A, B = data.split()

result = calculate_custom_product(A, B)

print(result)

