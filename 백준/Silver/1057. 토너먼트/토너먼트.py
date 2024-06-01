def find_round(N, kim, lim):

    round_num = 0

    while kim != lim:

        round_num += 1

        kim = (kim + 1) // 2

        lim = (lim + 1) // 2

    return round_num

N, kim, lim = map(int, input().split())

result = find_round(N, kim, lim)

print(result)

