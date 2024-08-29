# n차 드래곤 커브는 n-1차 드래곤 커브의 끝점에
# n-1차 드래곤 커브를 복제한 뒤 시계 방향으로 90도 회전시킨 뒤 연결한 도형

# 크기 100×100의 좌표평면 위에 n개의 드래곤 커브가 주어질 때
# 만들어지는 크기가 1인 정사각형의 개수의 개수
# 정사각형의 네 꼭지점이 모두 드래곤 커브에 속하는 도형 > 선분으로 이어지지 않아도 된다...

# 입력으로 주어지는 드래곤 커브의 모든 꼭지점은 좌표평면의 범위를 넘어서지 않는다

N = M = 100
directions = ((0, 1), (-1, 0), (0, -1), (1, 0))    # 오른쪽, 위쪽, 왼쪽, 아래쪽

used = [[0] * (M + 1) for _ in range(N + 1)]

C = int(input())
for _ in range(C):
    x, y, D, G = map(int, input().split())

    # 0차원부터 시작
    ds = [D]

    for g in range(G):
        if g == 0:
            ds.append((D + 1) % 4)
            continue

        for i in range(2 ** g):
            if i < 2 ** (g - 1):
                ds.append((ds[i] + 2) % 4)
            else:
                ds.append(ds[i])

    used[y][x] = 1
    for d in ds:
        dy, dx = directions[d]
        y += dy
        x += dx
        used[y][x] = 1

result = 0

for i in range(N):
    for j in range(M):
        if used[i][j] and used[i + 1][j] and used[i][j + 1] and used[i + 1][j + 1]:
            result += 1

print(result)