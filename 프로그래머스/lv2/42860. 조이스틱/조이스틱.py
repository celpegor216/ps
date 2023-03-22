# 힌트: dfs나 bfs로 풀어야 함

def solution(name):
    answer = 9999999999999
    cnt = 0
    length = len(name)
    
    used = [0] * length
    
    for i in range(length):
        if name[i] == 'A':
            used[i] = 1
            cnt += 1
    
    def dfs(level, now, total):
        nonlocal answer
        
        if total > answer:
            return
        
        if level == length:
            answer = min(total, answer)
            return
        
        # 지금 위치에서 바꾸지 않은 알파벳으로 이동해서 알파벳 변경
        for i in range(length):
            if not used[i]:
                used[i] = 1
                leftright = min(abs(now - i), length - now + i, length - i + now)
                updown = min(ord('Z') - ord(name[i]) + 1, ord(name[i]) - ord('A'))
                dfs(level + 1, i, total + leftright + updown)
                used[i] = 0
    
    dfs(cnt, 0, 0)
                
    return answer