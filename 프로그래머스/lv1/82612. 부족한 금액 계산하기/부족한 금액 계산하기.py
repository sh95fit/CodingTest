def solution(price, money, count):
    total_price = 0
    for i in range(count+1) :
        total_price = total_price + price*i
    if (money - total_price) >= 0 :
        answer = 0
    else : answer = total_price-money
    return answer