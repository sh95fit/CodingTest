def min_unique_suffix_length(N, student_numbers):   
    length = len(student_numbers[0])
    
    for k in range(1, length + 1):
        seen = set()

        for number in student_numbers:
            suffix = number[-k:]  
            seen.add(suffix)
        
        if len(seen) == N:  
            return k
    
    return length  

import sys

input = sys.stdin.read

data = input().splitlines()

N = int(data[0])
student_numbers = data[1:N + 1]

print(min_unique_suffix_length(N, student_numbers))

