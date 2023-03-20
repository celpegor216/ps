def solution(weights):
    answer = 0
    
    mults = [2 / 3, 2 / 4, 3 / 2, 3 / 4, 4 / 2, 4 / 3]
    
    dic = {}
    
    for weight in weights:
        if weight in dic.keys():
            dic[weight] += 1
        else:
            dic[weight] = 1
    
    for key in dic.keys():
        answer += dic[key] * (dic[key] - 1)
        
        for mult in mults:
            if key * mult in dic.keys():
                answer += dic[key] * dic[key * mult]
    
    return answer // 2