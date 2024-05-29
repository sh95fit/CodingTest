
N = int(input())

file_names = [input() for _ in range(N)]

pattern = ''

for i in range(len(file_names[0])):

    unique_chars = set(file_name[i] for file_name in file_names)

    if len(unique_chars) == 1:

        pattern += file_names[0][i]

    else:

        pattern += '?'

print(pattern)

