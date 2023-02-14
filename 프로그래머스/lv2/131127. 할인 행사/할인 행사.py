def solution(want, number, discount):
    answer = 0
    
    want = {want[i]: [0, number[i]] for i in range(len(want))}
    
    for i in range(10):
        if discount[i] in want.keys():
            want[discount[i]][0] += 1    
            
    flag = 0
    for key in want.keys():
        if want[key][0] != want[key][1]:
            flag = 1
            break

    if not flag:
        answer += 1
    
    for i in range(len(discount) - 10):            
        if discount[i] in want.keys():
                want[discount[i]][0] -= 1
        if discount[i + 10] in want.keys():
            want[discount[i + 10]][0] += 1
            
        flag = 0
        for key in want.keys():
            if want[key][0] != want[key][1]:
                flag = 1
                break
        
        if not flag:
            answer += 1
    
    return answer