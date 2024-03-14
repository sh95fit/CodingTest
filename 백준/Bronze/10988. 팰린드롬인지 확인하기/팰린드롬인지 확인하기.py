s = input()
#r = ''.join(list(s).reverse())
r = ''.join(list(s)[::-1])

if s == r:
    print(1)
else :
    print(0)
