h, m = list(map(int, input().split(' ')))
t = int(input())

if m+t < 60 :
    print(f"{h} {m+t}")
else :
    minute = (m+t)%60
    hour = h + (m+t)//60
    
    if hour >= 24 :
        hour = hour%24
        
    print(f"{hour} {minute}")