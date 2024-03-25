lines = []

while True:

    try:

        line = input()

        lines.append(line)

    except EOFError:

        break

max_length = max(len(line) for line in lines)

for i in range(max_length):

    for line in lines:

        if i < len(line):

            print(line[i], end='')

