# 힌트: bfs

from collections import deque
import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
tubes = [set(map(int, input().split())) for _ in range(M)]

q = deque()
used = [0] * M
cnt = [21e8] * (N + 1)

q.append(1)
cnt[1] = 1

while q:
    now = q.popleft()

    for m in range(M):
        if not used[m] and now in tubes[m]:
            used[m] = 1

            for item in tubes[m]:
                if cnt[item] > cnt[now] + 1:
                    cnt[item] = cnt[now] + 1
                    q.append(item)

if cnt[-1] == 21e8:
    print(-1)
else:
    print(cnt[-1])