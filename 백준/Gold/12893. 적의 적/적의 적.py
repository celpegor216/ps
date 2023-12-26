# 해답: https://bmy1320.tistory.com/entry/%EB%B0%B1%EC%A4%80-Gold-4-%EB%AC%B8%EC%A0%9C-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-12893-%EC%A0%81%EC%9D%98-%EC%A0%81-BFS-%EC%9D%B4%EB%B6%84%EA%B7%B8%EB%9E%98%ED%94%84

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
group = [0] * (N + 1)

for m in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

result = 1

for i in range(1, N + 1):
    if not group[i]:
        q = deque()
        q.append(i)

        group[i] = 1

        while q:
            now = q.popleft()

            for item in lst[now]:
                if not group[item]:
                    group[item] = group[now] * (-1)
                    q.append(item)
                elif group[item] == group[now]:
                    result = 0
                    break
        
    if result == 0:
        break

print(result)