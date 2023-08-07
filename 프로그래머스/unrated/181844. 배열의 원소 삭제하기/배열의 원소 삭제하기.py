def solution(arr, delete_list):
    result = []
    for e in arr :
        if e not in delete_list :
            result.append(e)
    return result