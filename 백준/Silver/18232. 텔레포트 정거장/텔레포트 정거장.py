from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)


def bfs():
    used = [0] * (N + 1)
    used[S] = 1

    q = deque()
    q.append(S)

    result = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()

            if now == E:
                return result
            
            for nxt in [now + 1, now - 1] + lst[now]:
                if 1 <= nxt <= N and not used[nxt]:
                    used[nxt] = 1
                    q.append(nxt)

        result += 1

print(bfs())