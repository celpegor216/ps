from collections import deque
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

children = [[] for _ in range(N + 1)]
parents = [[] for _ in range(N + 1)]

for _ in range(M):
    P, C = map(int, input().split())
    children[P].append(C)
    parents[C].append(P)

def find_cnt(lst):
    q = deque()
    q.append(X)
    used = [0] * (N + 1)

    while q:
        now = q.popleft()

        for child in lst[now]:
            if not used[child]:
                used[child] = 1
                q.append(child)
    
    return sum(used)

print(1 + find_cnt(parents), N - find_cnt(children))