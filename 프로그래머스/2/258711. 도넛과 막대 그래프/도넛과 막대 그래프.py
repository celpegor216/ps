from collections import deque

def solution(edges):
    answer = [0] * 4
    
    lst = [[] for _ in range(1000001)]
    cnt = [0] * 1000001
    for a, b in edges:
        lst[a].append(b)
        cnt[b] += 1
    
    # 생성한 정점 찾기
    # 나가는 방향은 2개 이상이고 들어오는 건 없는 정점
    for i in range(1, 1000001):
        if len(lst[i]) >= 2 and cnt[i] == 0:
            answer[0] = i
            break
                
    group = [x for x in range(1000001)]
    
    def find(a):
        if group[a] != a:
            group[a] = find(group[a])
        return group[a]
    
    def union(a, b):
        group_a, group_b = find(a), find(b)
        
        if group_a == group_b:
            return False

        if group_a < group_b:
            group[group_b] = group_a
        else:
            group[group_a] = group_b
        return True
    
    # 그래프 분류하기
    for item in lst[answer[0]]:
        q = deque()
        q.append(item)
        
        v = 1
        e = 0
        
        while q:
            now = q.popleft()
            
            for i in lst[now]:
                if union(now, i):
                    v += 1
                    q.append(i)
                e += 1

        if v == e:
            answer[1] += 1
        elif v == e + 1:
            answer[2] += 1
        else:
            answer[3] += 1
    
    return answer