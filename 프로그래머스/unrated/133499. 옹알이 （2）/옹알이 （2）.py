def solution(babbling):
    answer = 0
    
    for bab in babbling:
        idx = 0
        before = ''
        while idx < len(bab):
            two = bab[idx:idx+2]
            three = bab[idx:idx+3]
            if (two == 'ye' and before != 'ye') or (two == 'ma' and before != 'ma'):
                idx += 2
                before = two
            elif (three == 'aya' and before != 'aya') or (three == 'woo' and before != 'woo'):
                idx += 3
                before = three
            else:
                break
                
        if idx == len(bab):
            answer += 1
            
    return answer