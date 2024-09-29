import sys
input = sys.stdin.readline


N, M = map(int, input().split())
original = [[] for _ in range(N + 1)]
reversed = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    original[a].append(b)
    reversed[b].append(a)


def check(lst, start):
    used = [0] * (N + 1)
    used[start] = 1

    q = [start]
    while q:
        nq = []

        for now in q:
            for nxt in lst[now]:
                if used[nxt]:
                    continue
                    
                used[nxt] = 1
                nq.append(nxt)
        
        q = nq

    return used


from_start_to_target = check(original, 1)
from_end_to_target = check(reversed, N)

T = int(input())
for _ in range(T):
    target = int(input())
    print('Defend the CTP' if from_start_to_target[target] and from_end_to_target[target] else 'Destroyed the CTP')