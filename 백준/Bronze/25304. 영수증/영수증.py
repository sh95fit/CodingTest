tm = int(input())
num = int(input())
result = 0

for i in range(num) :
    a, b = list(map(int, input().split(' ')))
    result += a*b

if result == tm :
    print("Yes")
else :
    print("No")