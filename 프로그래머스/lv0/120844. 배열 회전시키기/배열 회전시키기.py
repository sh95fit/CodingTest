def solution(numbers, direction):
    r_answer = []
    r_answer.append(numbers[-1])
    l_answer = []
    l_answer.append(numbers[0])
    for i in range(0, len(numbers)-1) :
        if direction == "right" :
            r_answer.append(numbers[i])
        elif direction == "left" :
            l_answer.insert(0, numbers[len(numbers)-1-i])
    if direction == "right" :
        return r_answer
    else :
        return l_answer