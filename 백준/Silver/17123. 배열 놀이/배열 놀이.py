import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    total_r = [0] * N
    total_c = [0] * N
    for r in range(N):
        for c in range(N):
            total_r[r] += lst[r][c]
            total_c[c] += lst[r][c]

    for m in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1

        for r in range(r1, r2 + 1):
            total_r[r] += v * (c2 - c1 + 1)

        for c in range(c1, c2 + 1):
            total_c[c] += v * (r2 - r1 + 1)
    
    print(*total_r)
    print(*total_c)
