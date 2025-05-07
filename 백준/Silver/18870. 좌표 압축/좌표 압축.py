import sys

input = sys.stdin.read

def main():
    data = input().split()
    N = int(data[0])
    coords = list(map(int, data[1:]))
   
    sorted_unique = sorted(set(coords))    
    rank = {value: i for i, value in enumerate(sorted_unique)}

    print(' '.join(str(rank[x]) for x in coords))

main()