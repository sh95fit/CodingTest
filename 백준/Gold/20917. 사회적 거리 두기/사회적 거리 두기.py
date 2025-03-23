def can_place_seats(x, n, s, dist):   
    count = 1  
    last_position = x[0]  
    
    for i in range(1, n):
        if x[i] - last_position >= dist:
            count += 1
            last_position = x[i]

            if count == s:
                return True

    return False

def max_distance(n, s, x):
    x.sort()  
    low, high = 1, x[-1] - x[0]     
    answer = 0
    
    while low <= high:
        mid = (low + high) // 2

        if can_place_seats(x, n, s, mid):
            answer = mid  
            low = mid + 1
        else:
            high = mid - 1
            
    return answer

def main():
    T = int(input())  

    for _ in range(T):
        n, s = map(int, input().split())  
        x = list(map(int, input().split()))  
        
        result = max_distance(n, s, x)

        print(result)

if __name__ == "__main__":
    main()

