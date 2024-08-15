from collections import deque

N = int(input())
types = list(map(int, input().split()))    # 큐 0, 스택 1
lst = list(map(int, input().split()))

q = deque()    # 어차피 스택은 변하지 않으므로 큐만 관리
for n in range(N):
    if not types[n]:
        q.append(lst[n])

M = int(input())
adds = list(map(int, input().split()))

result = [0] * M
for m in range(M):
    q.appendleft(adds[m])
    result[m] = q.pop()

print(*result)