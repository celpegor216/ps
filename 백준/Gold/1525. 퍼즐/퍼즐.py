# 메모리 초과
# 해답: https://thought-process-ing.tistory.com/141

from collections import deque

board = ''
for _ in range(3):
    board += input().replace(' ', '')

q = deque()
q.append((board, 0))
used = dict()
used[board] = 0

answer = '123456780'
result = -1

while q:
    nowb, nowc = q.popleft()

    if nowb == answer:
        result = nowc
        break

    idx = nowb.index('0')
    y, x = idx // 3, idx % 3

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < 3 and 0 <= nx < 3:
            nidx = ny * 3 + nx
            tmp = list(nowb)
            tmp[idx], tmp[nidx] = tmp[nidx], tmp[idx]
            tmp = ''.join(tmp)
            if not used.get(tmp):
                used[tmp] = nowc + 1
                q.append((tmp, nowc + 1))

print(result)