x = input()

if x.startswith("0x"):
    print(int(x, 16))

elif x.startswith("0") and len(x) > 1:
    print(int(x, 8))

else:
    print(int(x, 10))