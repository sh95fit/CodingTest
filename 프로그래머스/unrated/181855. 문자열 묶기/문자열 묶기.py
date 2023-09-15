def solution(strArr):
    lenArr = list(map(len, strArr))
    return lenArr.count(max(set(lenArr), key=lenArr.count))