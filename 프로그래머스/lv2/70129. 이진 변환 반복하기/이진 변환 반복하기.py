def solution(s):
    n = 0
    count = 0
    answer = []
    while True :
        count += s.count("0")
        if s == "1" :
            break
        s = bin(len(s.replace('0',"")))
        s = s.replace("0b", "")
        n += 1
    answer.append(n)
    answer.append(count)
    return answer
        
