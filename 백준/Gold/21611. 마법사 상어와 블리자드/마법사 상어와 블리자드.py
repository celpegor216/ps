# 크기가 N×N, N은 항상 홀수, 블리자드를 총 M번 시전
N, M = map(int, input().split())
# 마법사 상어는 ((N+1)/2, (N+1)/2)에 있다
# 가장 처음에 상어가 있는 칸을 제외한 나머지 칸에는 구슬이 하나 들어갈 수 있다.
# 구슬은 1번 구슬, 2번 구슬, 3번 구슬이 있다.
lst = [list(map(int, input().split())) for _ in range(N)]

# 4가지 방향 ↑, ↓, ←, →가 있고, 정수 1, 2, 3, 4
directions = ((), (-1, 0), (1, 0), (0, -1), (0, 1))

# 각 위치에 소용돌이 순서대로 번호 붙이기
# 구슬은 소용돌이 모양, 상어 왼쪽에서 시작해서 반시계방향 토네이도
def fill_pos_to_idx():
    y = x = N // 2

    # 상어 빼고 왼쪽부터 시작
    temp_directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

    cnt = 0
    max_cnt = 1
    increase_max_cnt = 2
    d = 0
    idx = 0

    new_lst = []

    while 1:
        y += temp_directions[d][0]
        x += temp_directions[d][1]
        cnt += 1

        if not(0 <= y < N and 0 <= x < N):
            break

        pos_to_idx[y][x] = idx
        idx += 1
        new_lst.append(lst[y][x])

        if cnt == max_cnt:
            increase_max_cnt -= 1

            if not increase_max_cnt:
                increase_max_cnt = 2
                max_cnt += 1

            d = (d + 1) % 4
            cnt = 0

    return new_lst


pos_to_idx = [[0] * N for _ in range(N)]
lst = fill_pos_to_idx()


MAX_LENGTH = (N ** 2) - 1


result = 0
for _ in range(M):
    # 블리자드 마법을 시전하려면 방향 di와 거리 si
    D, S = map(int, input().split())

    # di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴
    # 구슬이 파괴되면 그 칸은 구슬이 들어있지 않은 빈 칸
    dy, dx = directions[D]
    ny = nx = N // 2
    length = len(lst)
    for _ in range(S):
        ny += dy
        nx += dx
        idx = pos_to_idx[ny][nx]

        if idx < length:
            lst[idx] = 0

    # 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸
    # 더 이상 구슬이 이동하지 않을 때까지 반복
    # 구슬이 폭발하는 단계
    # 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생
    # 같은 번호를 가진 구슬이 번호가 연속하는 칸에 있으면, 그 구슬을 연속하는 구슬
    # 구슬이 폭발해 빈 칸이 생겼으니 다시 구슬이 이동
    # 더 이상 폭발하는 구슬이 없을때까지 이동 > 폭발 반복
    while 1:
        flag = 0

        # 구슬 이동
        lst = [item for item in lst if item != 0]
        lst.append(-1)

        # 구슬 폭발
        now = -1
        cnt = 0
        for i in range(len(lst)):
            if lst[i] == lst[now]:
                cnt += 1
            else:
                if cnt > 3:
                    flag = 1
                    result += lst[now] * cnt
                    for j in range(now, i):
                        lst[j] = 0
                now = i
                cnt = 1
        
        lst.pop()

        if not flag:
            break

    # 구슬이 변화하는 단계
    # 하나의 그룹은 두 개의 구슬 A와 B
    # 구슬 A의 번호는 그룹에 들어있는 구슬의 개수이고, B는 그룹을 이루고 있는 구슬의 번호
    # 만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다.
    # >> 합칠 수가 없나보네,,, 왜지??
    new_lst = []
    for item in lst:
        if not new_lst or new_lst[-1] != item:
            new_lst.append(1)
            new_lst.append(item)
        else:
            new_lst[-2] += 1

    lst = new_lst[:MAX_LENGTH]

    if not lst:
        break


# 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)
print(result)