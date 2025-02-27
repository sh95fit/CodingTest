from collections import deque

def solution(players, m, k):
    server_list = deque([0]*(k-1))
    active_server = sum(server_list)
    cnt = 0
    for player in players :
        if active_server > 0 :
            if player > m*active_server :
                required_server = (player)//m - active_server
                cnt += required_server
                server_list.appendleft(required_server)
                server_list.pop()
                active_server = sum(server_list)
            else :
                server_list.appendleft(0)
                server_list.pop()
                active_server = sum(server_list)
        else :
            if player >= m :
                required_server = (player)//m
                cnt += required_server
                server_list.appendleft(required_server)
                server_list.pop()
                active_server = sum(server_list)
            else :
                server_list.appendleft(0)
                server_list.pop()
                active_server = sum(server_list)
        print(server_list)
    return cnt