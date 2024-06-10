N = int(input())

cnt = 0
number = 0

while True:
    cnt += 1
    title = str(cnt)
    if '666' in title:
        number += 1
        if number == N: 
            break

print(title)