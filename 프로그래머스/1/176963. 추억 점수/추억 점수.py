def solution(name, yearning, photo):
    answer = []
    name_score = dict(zip(name,yearning))
    
    for p in photo :
        sum = 0
        for h in p :
            sum += name_score.get(h,0)
        answer.append(sum)

    return answer