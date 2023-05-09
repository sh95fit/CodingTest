from itertools import permutations as pm

def solution(k, dungeons):
    pmd = []
    for i in pm(dungeons,len(dungeons)):
        pmd.append(list(i))

    answer=[]
    c = 0
    
    while c < len(pmd) :
        m = k
        count = 0
        for r in pmd[c] :   
            if m >= r[0] :
                m -= r[1]
                count +=1
            else :
                break
        
        c += 1
        answer.append(count)
    return max(answer)