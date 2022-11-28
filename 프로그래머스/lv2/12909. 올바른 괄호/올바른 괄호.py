def solution(s):
    bracket = []
    for i in s :
        if i == "(" :
            bracket.append(i)
        elif len(bracket) and i == ")" :
            bracket.pop()
        else :
            return False
    if len(bracket) :
        return False
    else :
        return True
