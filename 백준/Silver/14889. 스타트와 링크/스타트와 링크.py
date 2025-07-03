import sys
from itertools import combinations

def main() -> None:
    input = sys.stdin.readline
    N = int(input().strip())
    S = [list(map(int, input().split())) for _ in range(N)]
    
    pair = [[S[i][j] + S[j][i] for j in range(N)] for i in range(N)]
    people = list(range(1, N))          
    half = N // 2 - 1                  
    min_diff = float('inf')

    for comb in combinations(people, half):
        start = (0,) + comb             
        link  = [p for p in range(N) if p not in start]      
        power_start = 0

        for i in range(half + 1):
            for j in range(i + 1, half + 1):
                power_start += pair[start[i]][start[j]]
       
        power_link = 0

        for i in range(half + 1):
            for j in range(i + 1, half + 1):
                power_link += pair[link[i]][link[j]]

        diff = abs(power_start - power_link)

        if diff < min_diff:
            min_diff = diff

            if min_diff == 0:           
                break

    print(min_diff)

if __name__ == "__main__":
    main()