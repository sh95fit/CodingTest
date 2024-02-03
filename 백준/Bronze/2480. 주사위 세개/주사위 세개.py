n= list(map(int, input().split(' ')))

if n[0]==n[1] and n[1]==n[2] and n[2]==n[0] :
    print(10000+n[0]*1000)
elif n[0]==n[1] or n[1]==n[2] or n[2]==n[0] :
    if n[0]==n[1] :
        print(1000+n[0]*100)
    else :
        print(1000+n[2]*100)
else :
    print(max(n)*100)
   
       