from collections import deque

def solution(n, edge):
    lst = [[] for _ in range(n)]
    
    for e in edge:
        a, b = e
        a -= 1
        b -= 1
        
        lst[a].append(b)
        lst[b].append(a)
    
    answer = [21e8] * n
    answer[0] = 0
    
    q = deque()
    q.append([0, 0])
    
    while q:
        via, start_via_cost = q.popleft()
        
        for item in lst[via]:
            if answer[item] > start_via_cost + 1:
                q.append([item, start_via_cost + 1])
                answer[item] = start_via_cost + 1
    
    return answer.count(max(answer))