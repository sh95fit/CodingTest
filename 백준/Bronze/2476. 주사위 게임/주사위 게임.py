N = int(input())  
max_prize = 0  

for _ in range(N):
    dice = list(map(int, input().split()))  
    
    if len(set(dice)) == 1:  
        prize = 10000 + dice[0] * 1000
    elif len(set(dice)) == 2:  
        repeated = max(dice, key=dice.count)  
        prize = 1000 + repeated * 100

    else: 
        prize = max(dice) * 100

    max_prize = max(max_prize, prize)  

print(max_prize)

