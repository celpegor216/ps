def solution(n, t, m, p):
    answer = ''
    
    cnt = 0    # 지금까지 말한 사람 수
    i = 0      # 숫자
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    while 1:
        num = i
        temp = '' if num else '0'
        
        while num:
            now = num % n
            if now > 9:
                now = dic[now]
            else:
                now = str(now)
            
            temp += now
            num //= n
        
        for s in temp[::-1]:
            cnt += 1
            
            if cnt > m:
                cnt = 1
            
            if cnt == p:
                answer += s
        
        if len(answer) >= t:
            break
        
        i += 1
    
    return answer[:t]