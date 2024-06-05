def is_self_replicating(n):
    square = n * n
    n_str = str(n)
    square_str = str(square)
    return square_str.endswith(n_str)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    test_cases = [int(data[i]) for i in range(1, T + 1)]
    
    results = []
    for n in test_cases:
        if is_self_replicating(n):
            results.append("YES")
        else:
            results.append("NO")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
