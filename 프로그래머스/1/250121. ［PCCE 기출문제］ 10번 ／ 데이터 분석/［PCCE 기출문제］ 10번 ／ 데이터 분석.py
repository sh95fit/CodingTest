def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_dic = {"code":0, "date":1, "maximum":2, "remain":3}
    
    for d in data :
        if d[ext_dic[ext]] < val_ext:
            answer.append(d)
    
    answer.sort(key=lambda x:x[ext_dic[sort_by]])
    
    return answer