def find(parent, x):

    if parent[x] != x:

        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, rank, x, y):

    rootX = find(parent, x)

    rootY = find(parent, y)

    

    if rootX != rootY:

        if rank[rootX] > rank[rootY]:

            parent[rootY] = rootX

        elif rank[rootX] < rank[rootY]:

            parent[rootX] = rootY

        else:

            parent[rootY] = rootX

            rank[rootX] += 1

def main():

    import sys

    input = sys.stdin.read

    data = input().split()

    idx = 0

    N = int(data[idx])

    M = int(data[idx + 1])

    idx += 2

    

    truth_count = int(data[idx])

    truths = list(map(int, data[idx + 1:idx + 1 + truth_count]))

    idx += 1 + truth_count

    

    parent = list(range(N + 1))

    rank = [0] * (N + 1)

    parties = []

    for _ in range(M):

        party_count = int(data[idx])

        party = list(map(int, data[idx + 1:idx + 1 + party_count]))

        parties.append(party)

        idx += 1 + party_count

        

        for i in range(party_count - 1):

            union(parent, rank, party[i], party[i + 1])

    truth_root = set(find(parent, person) for person in truths)

    result = 0

    for party in parties:

        if all(find(parent, person) not in truth_root for person in party):

            result += 1

    print(result)

if __name__ == "__main__":

    main()

