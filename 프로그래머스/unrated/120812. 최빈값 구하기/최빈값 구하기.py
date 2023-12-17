import pandas as pd
def solution(array):
    array = pd.DataFrame(array)
    if len(array.mode()) > 1 :
        return -1
    else :
        return int(array.mode()[0][0])