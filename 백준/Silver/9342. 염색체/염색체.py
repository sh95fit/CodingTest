import re

def check_infection(n, cases):
    pattern = re.compile(r'^[A-F]?A+F+C+[A-F]?$')
    results = []
    for case in cases:
        if pattern.match(case):
            results.append("Infected!")
        else:
            results.append("Good")
    return results

T = int(input().strip())  
cases = [input().strip() for _ in range(T)]

for result in check_infection(T, cases):
    print(result)
