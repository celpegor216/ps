from collections import deque

def solution(begin, target, words):
    answer = 0
    
    q = deque()
    q.append((begin, 0))
    length = len(words)
    used = [0] * length
    
    while q:
        noww, nowc = q.popleft()
        
        if noww == target:
            answer = nowc
            break
        
        for i in range(length):
            if not used[i]:
                flag = 0
                
                for j in range(len(noww)):
                    if noww[j] != words[i][j]:
                        flag += 1
                
                if flag == 1:
                    used[i] = 1
                    q.append((words[i], nowc + 1))
        
    return answer