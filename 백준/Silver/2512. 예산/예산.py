def allocate_budget(N, budgets, M):   
    low, high = 0, max(budgets)
     
    while low <= high:
        mid = (low + high) // 2
        total = 0
               
        for budget in budgets:
            total += min(budget, mid)
               
        if total <= M:
            low = mid + 1
       
        else:
            high = mid - 1
       
    return high

N = int(input())  
budgets = list(map(int, input().split()))  
M = int(input())  

print(allocate_budget(N, budgets, M))

