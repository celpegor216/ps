def solution(s):
    answer = 0
    
    now = s[0]
    now_cnt = 1
    diff_cnt = 0
    
    for i in range(1, len(s)):
        if s[i] == now:
            now_cnt += 1
        else:
            diff_cnt += 1
        
        if now_cnt == diff_cnt:
            answer += 1
            if i < len(s) - 1:
                now = s[i + 1]
            now_cnt = 0
            diff_cnt = 0
            
    if now_cnt != diff_cnt:
        answer += 1
    
    return answer