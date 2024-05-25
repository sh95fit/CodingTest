def is_balanced(s):

    stack = []

    for char in s:

        if char in "([":  

            stack.append(char)

        elif char in ")]":  

            if not stack:

                return False

            top = stack.pop()

            if char == ")" and top != "(":

                return False

            if char == "]" and top != "[":

                return False

    return not stack

import sys

input = sys.stdin.read

data = input().splitlines()

for line in data:

    if line == ".":

        break

    if is_balanced(line):

        print("yes")

    else:

        print("no")

