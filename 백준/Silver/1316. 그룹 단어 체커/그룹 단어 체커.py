def is_group_word(word):
    visited = []
    for char in word:
        if char not in visited:
            visited.append(char)
        else:
            if visited[-1] != char:
                return False
    return True

N = int(input())
count = 0
for _ in range(N):
    word = input().strip()
    if is_group_word(word):
        count += 1

print(count)