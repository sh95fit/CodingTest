def solution(name, yearning, photo):
    answer = []
    name_score = {}
    
    for i in range(len(name)):
        name_score[name[i]] = yearning[i]
    
    for p in photo :
        sum = 0
        for h in p :
            sum += name_score.get(h,0)
        answer.append(sum)

    return answer