def solution(name, yearning, photo):
    answer = []
    
    dic = {}
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for p in photo:
        total = 0
        
        for name in p:
            if dic.get(name):
                total += dic[name]
        
        answer.append(total)
    
    return answer