N = int(input())

def is_valid(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack: 
                return False
            stack.pop()
    return len(stack) == 0

for _ in range(N):
    s = input()
    if is_valid(s):
        print("YES")
    else:
        print("NO")