def solution(hp) :
    ant = {'장군' : 5, '병정' : 3, '일' : 1}
    count = 0

    while hp != 0 :
        if int(hp)//ant['장군'] >= 1 :
            count += int(hp)//ant['장군']
            hp = int(hp)%ant['장군']
        elif int(hp)//ant['병정'] >= 1 :
            count += int(hp)//ant['병정']
            hp = int(hp)%ant['병정']
        else :
            count += int(hp)//ant['일']
            hp = int(hp)%ant['일']
    return count