from collections import deque

N, M, K = map(int, input().split())

# y, x 좌표의 음식물의 번호, 사용 여부
dic = dict()

for k in range(1, K + 1):
    y, x = map(lambda x: int(x) - 1, input().split())
    dic[y * M + x] = [k, 0]

result = 0

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

for key, value in dic.items():
    if value[1]:
        continue

    dic[key][1] = 1

    q = deque()
    q.append((key // M, key % M))

    cnt = 1

    while q:
        y, x = q.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            nkey = ny * M + nx

            if 0 <= ny < N and 0 <= nx < M and dic.get(nkey) and not dic[nkey][1]:
                dic[nkey][1] = 1
                q.append((ny, nx))
                cnt += 1
    
    result = max(result, cnt)

print(result)