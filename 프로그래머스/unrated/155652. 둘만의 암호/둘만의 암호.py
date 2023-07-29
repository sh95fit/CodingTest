def solution(s, skip, index):
    skip_list = list(map(ord, skip))
    s_list = list(map(ord, s))
    
    for i, s in enumerate(s_list) :
        index_num = index 
        while index_num!=0 :
            s += 1
            if s > 122 :
                s = 97
            if s not in skip_list :
                index_num -=1
        s_list[i] = s
    
    return ''.join(list(map(chr, s_list)))