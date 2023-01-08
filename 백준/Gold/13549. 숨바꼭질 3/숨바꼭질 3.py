# 힌트: 동생의 위치가 0일 때

from collections import deque

N, K = map(int, input().split())

def bfs(start, end):
    q = deque()
    q.append((start, 0))

    used = [21e8] * 100001
    used[start] = 0

    result = 21e8

    while q:
        nowp, nowc = q.popleft()

        if nowp == end and result > nowc:
            result = nowc
            continue

        warp = nowp * 2
        if 0 <= warp < 100001 and used[warp] > nowc:
            q.append((warp, nowc))
            used[warp] = nowc

        for walk in (nowp + 1, nowp - 1):
            if 0 <= walk < 100001 and used[walk] > nowc + 1:
                q.append((walk, nowc + 1))
                used[walk] = nowc + 1

    return result

if K == 0:
    print(N)
else:
    print(bfs(N, K))