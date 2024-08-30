# N×N 크기
N = int(input())
M = N
# 각 학생이 좋아하는 학생 4명
# 학생의 번호는 중복되지 않으며, 어떤 학생이 좋아하는 학생 4명은 모두 다른 학생
# 어떤 학생이 자기 자신을 좋아하는 경우는 없다.
lst = []

# order[i]: i번 학생의 입력 순서(나중에 점수 계산할 때 좋아하는 친구 찾기 위함)
order = [-1] * (N * N + 1)

for n in range(N * N):
    # 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호
    lst.append(list(map(int, input().split())))
    order[lst[-1][0]] = n

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 처음에는 교실의 모든 칸은 빈 칸
board = [[0] * M for _ in range(N)]


# 학생의 순서대로 배치
for student, *likes in lst:
    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    # 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    # 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

    res_cnt_likes = -1
    res_cnt_blanks = -1
    res_pos = []

    for i in range(N):
        for j in range(M):
            # 비어있는 칸 중에서
            if board[i][j]:
                continue

            cnt_likes = 0
            cnt_blanks = 0

            for dy, dx in directions:
                ny, nx = i + dy, j + dx
                if 0 <= ny < N and 0 <= nx < M:
                    if board[ny][nx] in likes:
                        cnt_likes += 1
                    elif not board[ny][nx]:
                        cnt_blanks += 1

            # > 정렬 기준: 좋아하는 친구 수가 큰 순 >
            #            비어있는 칸의 수가 큰 순 >
            #            행 번호가 작은 순 >
            #            열 번호가 작은 순
            if res_cnt_likes < cnt_likes:
                res_cnt_likes = cnt_likes
                res_cnt_blanks = cnt_blanks
                res_pos = [i, j]
            elif res_cnt_likes == cnt_likes:
                if res_cnt_blanks < cnt_blanks:
                    res_cnt_likes = cnt_likes
                    res_cnt_blanks = cnt_blanks
                    res_pos = [i, j]
                elif res_cnt_blanks == cnt_blanks:
                    if res_pos[0] > i:
                        res_cnt_likes = cnt_likes
                        res_cnt_blanks = cnt_blanks
                        res_pos = [i, j]
                    elif res_pos[0] == i:
                        if res_pos[1] > j:
                            res_cnt_likes = cnt_likes
                            res_cnt_blanks = cnt_blanks
                            res_pos = [i, j]

    board[res_pos[0]][res_pos[1]] = student


# 학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다
# 학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다.
result = 0
for i in range(N):
    for j in range(M):
        now = board[i][j]
        cnt_likes = 0

        for dy, dx in directions:
            ny, nx = i + dy, j + dx
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] in lst[order[now]]:
                cnt_likes += 1

        if cnt_likes:
            result += 10 ** (cnt_likes - 1)

print(result)
