def solution(arr):
    queue = []
    queue.append(arr[0])
    for i in range(len(arr)) :
        if arr[i] != queue[-1] :
            queue.append(arr[i])
    return queue