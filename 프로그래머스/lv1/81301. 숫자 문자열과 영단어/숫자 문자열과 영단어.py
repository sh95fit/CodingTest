def solution(s):
    alpha = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for i in range(10) :
        s = s.replace(list(alpha.keys())[i],list(alpha.values())[i])    
    return int(s)