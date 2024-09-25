import sys
input = sys.stdin.readline


def check():
    used = [0] * (N + 1)

    for i in range(1, N + 1):
        if used[i]:
            continue

        used[i] = 1
        q = [i]

        while q:
            nq = []

            for now in q:
                for nxt in lst[now]:
                    if not used[nxt]:
                        used[nxt] = used[now] * -1
                        nq.append(nxt)
                    elif used[nxt] == used[now]:
                        return 'impossible'

            q = nq

    return 'possible'


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)

    print(check())