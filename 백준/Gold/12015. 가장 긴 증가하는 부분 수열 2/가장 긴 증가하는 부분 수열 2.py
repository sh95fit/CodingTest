import bisect

def solve(N, A):   
    lis = []
  
    for num in A:       
        pos = bisect.bisect_left(lis, num)
               
        if pos < len(lis):
            lis[pos] = num

        else:           
            lis.append(num)
      
    return len(lis)

N = int(input())  
A = list(map(int, input().split()))  

print(solve(N, A))

