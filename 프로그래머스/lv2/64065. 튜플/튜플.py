def solution(s):
    answer = []
    
    # 2},{2,1},{2,1,3},{2,1,3,4
    
    lsts = s[2:-2].split('},{')
    lsts.sort(key = lambda x: len(x))
    
    for lst in lsts:
        temp = list(map(int, lst.split(',')))
        for item in temp:
            if item not in answer:
                answer .append(item)
                break
    
    return answer