def solution(s):
    s = s.split(" ")
    for i in range(len(s)) :
        k = list(s[i])
        for j in range(len(k)) :
            if j%2 == 0 :
                k[j] = k[j].upper()
            else :
                k[j] = k[j].lower()
        s[i] = ''.join(k)
    s = ' '.join(s)
    return s