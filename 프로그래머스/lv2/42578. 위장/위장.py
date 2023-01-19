# 1번만 시간초과남
# 해답: https://school.programmers.co.kr/questions/33347

def solution(clothes):
    answer = 1
    
    dic = {}
    
    for cloth in clothes:
        name, category = cloth
        
        if category in dic.keys():
            dic[category] += 1
        else:
            dic[category] = 1
            
    for key in dic.keys():
        answer *= (1 + dic[key])
    
    return answer - 1