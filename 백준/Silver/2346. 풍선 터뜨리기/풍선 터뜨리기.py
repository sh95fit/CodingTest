def solve_balloons(N, balloons):    
    balloons_status = list(range(1, N + 1))  
    exploded = []  
    current_idx = 0  
    
    while balloons_status:        
        current_balloon = balloons_status[current_idx]
        exploded.append(current_balloon)               
        move = balloons[current_balloon - 1]               
        balloons_status.remove(current_balloon)
               
        if len(balloons_status) > 0:            
            if move > 0:
                current_idx = (current_idx + move - 1) % len(balloons_status)
            else:
                current_idx = (current_idx + move) % len(balloons_status)

    return exploded

N = int(input())  
balloons = list(map(int, input().split()))  

result = solve_balloons(N, balloons)
print(" ".join(map(str, result)))

