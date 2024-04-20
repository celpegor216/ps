from collections import deque
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
dic = dict()

for _ in range(N):
    dic[tuple(map(int, input().split()))] = 21e8

q = deque()
q.append((0, 0, 0))

result = -1

while q:
    nowx, nowy, nowc = q.popleft()

    if nowy == T:
        result = nowc
        break

    for dy in range(-2, 3):
        if not 0 <= nowy + dy <= T:
            continue
        
        for dx in range(-2, 3):
            if not 0 <= nowx + dx <= 1000000:
                continue

            key = (nowx + dx, nowy + dy)

            if dic.get(key, -1) > nowc + 1:
                dic[key] = nowc + 1
                q.append((*key, nowc + 1))

print(result)