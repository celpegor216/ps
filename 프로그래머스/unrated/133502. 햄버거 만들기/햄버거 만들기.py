# 해답: https://khomep.shop/%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%a8%b8%ec%8a%a4-%ed%96%84%eb%b2%84%ea%b1%b0%eb%a7%8c%eb%93%a4%ea%b8%b0-%eb%ac%b8%ec%a0%9c-python/

def solution(ingredient):
    answer = 0
    
    idx = 0
    while idx < len(ingredient) - 3:
        if ingredient[idx] == 1 and ingredient[idx:idx + 4] == [1, 2, 3, 1]:
            del ingredient[idx:idx + 4]
            idx = idx - 3
            answer += 1
        else:
            idx += 1
            
    return answer