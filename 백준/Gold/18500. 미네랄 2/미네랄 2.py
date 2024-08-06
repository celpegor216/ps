N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

def check():
    used = [[0] * M for _ in range(N)]

    for i in range(N - 1):
        for j in range(M):
            if lst[i][j] == 'x' and not used[i][j]:
                used[i][j] = 1

                q = []
                q.append((i, j))
                idx = 0

                has_bottom = 0
                while idx < len(q):
                    y, x = q[idx]

                    if y == N - 1:
                        has_bottom = 1

                    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == 'x':
                            used[ny][nx] = 1
                            q.append((ny, nx))

                    idx += 1

                # 공중에 떠 있는 클러스터라면 바닥으로 떨어뜨리기
                if not has_bottom:
                    # 전체 클러스터가 떨어질 거리 정하기
                    q.sort(key=lambda x: -x[0])
                    down_cnt = N

                    for y, x in q:
                        ny = y + 1
                        while ny < N:
                            if (ny, x) in q:
                                ny = 21e8
                                break
                            elif lst[ny][x] == 'x':
                                break
                            ny += 1
                        down_cnt = min(down_cnt, ny - 1 - y)

                    # 전체 클러스터 떨어뜨리기
                    for y, x in q:
                        lst[y][x] = '.'
                        lst[y + down_cnt][x] = 'x'
                    return

K = int(input())
heights = list(map(int, input().split()))
for k in range(K):
    # 막대기 던지기
    h = -heights[k]

    # 왼쪽 > 오른쪽 > 왼쪽 > ...
    flag = 0
    rg = range(M) if not k % 2 else range(M - 1, -1, -1)
    for m in rg:
        if lst[h][m] == 'x':
            lst[h][m] = '.'
            flag = 1
            break

    # 미네랄을 부쉈다면 공중에 떠 있는 클러스터가 발생했는지 확인
    if flag:
        check()

for line in lst:
    print(''.join(line))