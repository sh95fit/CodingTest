slist = list(range(1,31))

while True :
    try :
        n = int(input())
        slist.remove(n)
    except EOFError:
        break

slist.sort()

for s in slist:
    print(s)
    