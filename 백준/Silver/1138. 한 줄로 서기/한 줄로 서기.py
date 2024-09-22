def arrange_people(N, memories):
    result = []
    
    for height in range(N, 0, -1): 
        left_bigger = memories[height - 1]  
        result.insert(left_bigger, height) 
    
    return result

N = int(input())
memories = list(map(int, input().split()))

result = arrange_people(N, memories)

print(' '.join(map(str, result)))

