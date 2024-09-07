from collections import deque

S, E = map(int, input().split())
N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

def bfs():
    q = deque()
    q.append(S)

    used = [0] * (N + 1)
    used[S] = 1

    result = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()

            if now == E:
                return result

            for nxt in lst[now]:
                if not used[nxt]:
                    used[nxt] = 1
                    q.append(nxt)

        result += 1

    return -1

print(bfs())