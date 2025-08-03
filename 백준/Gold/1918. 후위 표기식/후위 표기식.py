def infix_to_postfix(expression):

    precedence = {

        '+': 1,

        '-': 1,

        '*': 2,

        '/': 2

    }

    stack = []

    output = []

    for ch in expression:

        if ch.isalpha():  # 피연산자

            output.append(ch)

        elif ch == '(':  # 왼쪽 괄호

            stack.append(ch)

        elif ch == ')':  # 오른쪽 괄호

            while stack and stack[-1] != '(':

                output.append(stack.pop())

            stack.pop()  # '(' 제거

        elif ch in precedence:  # 연산자

            while (stack and stack[-1] != '(' and

                   precedence.get(stack[-1], 0) >= precedence[ch]):

                output.append(stack.pop())

            stack.append(ch)

    # 스택에 남은 연산자 출력

    while stack:

        output.append(stack.pop())

    return ''.join(output)

# 입력

expression = input().strip()

print(infix_to_postfix(expression))