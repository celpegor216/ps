# 격자의 크기 n, 최대 20, n * n
N = int(input())
M = N
# 블록은 적어도 하나 이상 주어진다
# 격자의 빈칸은 0으로 나타내며, 블록들은 2의 거듭제곱 형태


def rotate(cnt, lst):
    for _ in range(cnt):
        lst = list(map(list, zip(*lst[::-1])))
    return lst


# dfs로 5번 이동
L = 5
result = 0
def dfs(level, lst):
    global result

    # 5번 움직인 이후에 격자판에서 가장 큰 값의 최댓값을 구하는 프로그램
    # 한 번 움직인 이후로 같은 방향으로 계속 움직이면 어차피 그대로니까
    # 매번 판이 바뀔 때마다 최댓값 계산
    for line in lst:
        result = max(result, max(line))

    if level == L:
        return

    for i in range(4):
        # 90도 * i번 회전
        nxt = rotate(i, [line[:] for line in lst])

        # 세 개 이상의 같은 숫자가 중력작용 방향으로 놓여 있으면,
        # 중력에 의해 부딪히게 될 벽(바닥)에서 가까운 숫자부터 두 개씩만 합쳐집니다
        # 단 한 번의 중력작용으로 이미 합쳐진 숫자가 연쇄적으로 합쳐지진 않습니다

        # 움직였는데 이전과 동일하다면 dfs 타고 들어가지 않음
        flag = 0
        for m in range(M):
            last_merged = N + 1
            for n in range(N - 2, -1, -1):
                if nxt[n][m]:
                    y = n
                    while y < N - 1:
                        if nxt[y + 1][m]:
                            if y + 1 != last_merged and nxt[y + 1][m] == nxt[y][m]:
                                nxt[y][m] = 0
                                nxt[y + 1][m] *= 2
                                last_merged = y + 1
                                flag = 1
                            break
                        else:
                            nxt[y][m], nxt[y + 1][m] = nxt[y + 1][m], nxt[y][m]
                            flag = 1
                            y += 1

        nxt = rotate(4 - i, nxt)

        if flag:
            dfs(level + 1, nxt)


dfs(0, [list(map(int, input().split())) for _ in range(N)])

print(result)