def find_min_bribes(N, votes):
    dasom_votes = votes[0]
    other_votes = votes[1:]
    bribes = 0

    while other_votes and dasom_votes <= max(other_votes):
        max_votes = max(other_votes)
        max_index = other_votes.index(max_votes)
        other_votes[max_index] -= 1
        dasom_votes += 1
        bribes += 1

    return bribes

N = int(input().strip())
votes = [int(input().strip()) for _ in range(N)]

print(find_min_bribes(N, votes))

