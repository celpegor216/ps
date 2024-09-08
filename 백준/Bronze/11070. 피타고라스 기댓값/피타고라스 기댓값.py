T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # lst[i]: i번째 팀의 총 득점, 총 실점
    lst = [[0] * 2 for _ in range(N)]

    for _ in range(M):
        a, b, p, q = map(int, input().split())
        a -= 1
        b -= 1
        lst[a][0] += p
        lst[a][1] += q
        lst[b][0] += q
        lst[b][1] += p
    
    minv = 21e8
    maxv = 0

    for n in range(N):
        if lst[n][0] == lst[n][1] == 0:
            minv = 0
            continue
        
        v = lst[n][0] ** 2 / (lst[n][0] ** 2 + lst[n][1] ** 2)
        minv = min(minv, v)
        maxv = max(maxv, v)
    
    print(int(maxv * 1000))
    print(int(minv * 1000))