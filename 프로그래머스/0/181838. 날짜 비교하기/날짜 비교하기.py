from datetime import datetime
def solution(date1, date2):
    date1 = list(map(str, date1))
    date2 = list(map(str, date2))
    
    date1 = int(''.join(date1))
    date2 = int(''.join(date2))
    

    
    if date1 < date2 :
        return 1
    else :
        return 0
    