def solution(bin1, bin2):
    bin1 = '0b' + bin1
    bin2 = '0b' + bin2
    result = str(bin(int(bin1,2)+int(bin2,2)))
    result = result.replace('0b', '')
    
    return result