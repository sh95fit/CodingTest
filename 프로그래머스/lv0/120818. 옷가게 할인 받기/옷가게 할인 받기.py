def solution(price):
    if price >= 500000 :
        return int(0.8*price)
    elif price >= 300000 :
        return int(0.9*price)
    elif price >= 100000 :
        return int(0.95*price)
    else :
        return price