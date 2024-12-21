from collections import Counter

def solve():   
    N = int(input())       
    cards = list(map(int, input().split()))  
    
    M = int(input())       
    queries = list(map(int, input().split()))  
    
    card_count = Counter(cards)       
    result = []
       
    for query in queries:
        result.append(card_count.get(query, 0))  
    
    print(*result)

solve()

