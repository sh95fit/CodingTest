def solution(spell, dic):
    answer = 0
    
    dic = [x for x in dic if len(x)==len(spell)]
    # print(dic)
    
    for s in spell :
        for d in range(len(dic)) :
            if s in dic[d] :
                dic[d] = dic[d].replace(s, '',1)
                
    if '' in dic :
        return 1
    else :
        return 2