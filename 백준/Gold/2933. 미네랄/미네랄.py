from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

C = int(input())
hit = list(map(int, input().split()))

for c in range(C):
    # 미네랄 파괴
    flag = 0

    r = range(M) if not c % 2 else range(M - 1, -1, -1)
    for m in r:
        if lst[-hit[c]][m] == 'x':
            lst[-hit[c]][m] = '.'
            flag = 1
            break

    if flag:
        # 분리된 클러스터 확인
        cluster = [[0] * M for _ in range(N)]

        for m in range(M):
            if lst[-1][m] == 'x':
                q = deque()
                q.append((N - 1, m))
                cluster[-1][m] = 1

                while q:
                    y, x = q.popleft()

                    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M and not cluster[ny][nx] and lst[ny][nx] == 'x':
                            q.append((ny, nx))
                            cluster[ny][nx] = 1
        
        check = 0
        seperated_cluster = [[0] * M for _ in range(N)]
        for n in range(N):
            for m in range(M):
                if lst[n][m] == 'x' and not cluster[n][m]:
                    seperated_cluster[n][m] = 1
                    check = 1

        # 분리된 클러스터 낙하
        if check:
            minv = 21e8
            for n in range(N):
                for m in range(M):
                    if seperated_cluster[n][m]:
                        for i in range(n + 1, N):
                            if cluster[i][m]:
                                minv = min(minv, i - n - 1)
                        minv = min(minv, N - n - 1)

            for n in range(N - 1, -1, -1):
                for m in range(M):
                    if seperated_cluster[n][m]:
                        lst[n][m] = '.'
                        lst[n + minv][m] = 'x'

for line in lst:
    print(''.join(line))