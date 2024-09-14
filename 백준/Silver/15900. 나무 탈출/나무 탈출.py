from collections import deque
import sys
input = sys.stdin.readline


N = int(input())

lst = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

# 모든 리프 노드의 level 총합
total = 0

# 루트 노드는 1번
q = deque()
q.append(1)

used = [0] * (N + 1)
used[1] = 1

level = 0
while q:
    for _ in range(len(q)):
        now = q.popleft()
        
        flag = 0
        for child in lst[now]:
            if used[child]:
                continue
        
            flag = 1
            used[child] = 1
            q.append(child)
        
        if not flag:
            total += level
    
    level += 1

print('Yes' if total % 2 else 'No')