# 힌트: 123의 L은 1230이고 R은 3012이다

from collections import deque

T = int(input())

def bfs(A, B):
    q = deque()
    used = [0] * 10001

    q.append((A, ''))
    used[A] = 1

    while q:
        nowa, nowp = q.popleft()

        if nowa == B:
            return nowp

        # D연산 수행
        D = nowa * 2 % 10000
        if not used[D]:
            q.append((D, nowp + 'D'))
            used[D] = 1

        # S연산 수행
        S = nowa - 1 if nowa != 0 else 9999
        if not used[S]:
            q.append((S, nowp + 'S'))
            used[S] = 1

        # L연산 수행
        string = str(nowa)

        if len(string) < 4:
            string = '0' * (4 - len(string)) + string

        L = int(string[1:] + string[0])
        if not used[L]:
            q.append((L, nowp + 'L'))
            used[L] = 1

        # R연산 수행
        R = int(string[-1] + string[:-1])
        if not used[R]:
            q.append((R, nowp + 'R'))
            used[R] = 1

for t in range(T):
    A, B = map(int, input().split())

    result = bfs(A, B)

    print(result)