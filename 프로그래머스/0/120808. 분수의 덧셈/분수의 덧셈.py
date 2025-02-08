import math

def solution(numer1, denom1, numer2, denom2):    
    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2
    
    # 최대공약수 계산
    gcd = math.gcd(numerator, denominator)

    # 기약분수로 변환
    return [numerator // gcd, denominator // gcd]