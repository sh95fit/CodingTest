def solution(keyinput, board):
    key_dic= {'left':-1, 'right':1, 'up':1, 'down':-1}
    answer = [0,0]
    for key in keyinput :
        if key == 'left' :
            if -(board[0]//2) < answer[0] :
                answer[0] += key_dic[key]
            else :
                pass
        if key == 'right' :
            if board[0]//2 > answer[0] :
                answer[0] += key_dic[key]
            else :
                pass
        
        if key == 'up' :
            if board[1]//2 > answer[1] :
                answer[1] += key_dic[key]
            else :
                pass
        if key == 'down' :
            if -(board[1]//2) < answer[1] :
                answer[1] += key_dic[key]
            else :
                pass
    return answer