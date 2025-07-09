def get_score(name1, name2):
    combined = name1 + name2

    L = combined.count('L')
    O = combined.count('O')
    V = combined.count('V')
    E = combined.count('E')

    score = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100

    return score

yeondoo = input().strip()
n = int(input())
team_names = [input().strip() for _ in range(n)]

best_score = -1
best_team = ""

for team in sorted(team_names):  
    score = get_score(yeondoo, team)

    if score > best_score:
        best_score = score
        best_team = team

print(best_team)