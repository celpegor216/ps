# 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대
# 회전이나 대칭을 시켜도 된다

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 뒤집기 포함
blocks = [
    [[1, 1, 1, 1]],
    [[1], [1], [1], [1]],
    [[1, 1], [1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 0], [1, 1], [0, 1]],
    [[0, 1], [1, 1], [1, 0]],
    [[1, 0], [1, 1], [1, 0]]
]

rotate_cnts = [1, 1, 1, 4, 4, 2, 2, 4]

result = 0

# 블럭 별로
for idx in range(len(blocks)):
    now = blocks[idx]
    a, b = len(now), len(now[0])

    # 돌릴 필요가 있다면 한 번씩 돌려가면서
    for _ in range(rotate_cnts[idx]):
        # 모든 좌표 탐색
        for i in range(N - a + 1):
            for j in range(M - b + 1):
                total = 0

                for y in range(a):
                    for x in range(b):
                        total += lst[i + y][j + x] * now[y][x]

                result = max(result, total)

        # 블록 시계 방향으로 돌리기
        a, b = b, a
        now = list(map(list, zip(*now[::-1])))

print(result)