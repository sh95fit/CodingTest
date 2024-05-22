import sys

N, M = map(int, sys.stdin.readline().split())
pokemon_dict = {input(): i + 1 for i in range(N)}
query = [input() for _ in range(M)]

pokemon_list = list(pokemon_dict.keys())

for i in range(M): 
    try: 
        print(pokemon_dict[query[i]])
    except KeyError: 
        print(pokemon_list[int(query[i]) - 1])

