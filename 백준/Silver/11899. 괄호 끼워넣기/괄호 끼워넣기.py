stick = input()

def min_stack(s):
    cnt = 0
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack: 
                cnt += 1
            else :
                stack.pop()
    cnt += len(stack)
    return cnt

print(min_stack(stick))