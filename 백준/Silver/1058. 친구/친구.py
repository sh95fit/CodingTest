def find_most_famous_person(N, friendships):
    max_2_friends = 0

    for i in range(N):
        visited = set()

        for j in range(N):
            if friendships[i][j] == 'Y':
                visited.add(j)

                for k in range(N):
                    if friendships[j][k] == 'Y':
                        visited.add(k)

        visited.discard(i)  
        max_2_friends = max(max_2_friends, len(visited))

    return max_2_friends

N = int(input().strip())
friendships = [input().strip() for _ in range(N)]

print(find_most_famous_person(N, friendships))

