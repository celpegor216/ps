N = 4
# 12시 방향부터 시계 방향 순서대로
# n번 톱니바퀴의 2번 - n + 1번 톱니바퀴의 6번
lst = [input() for _ in range(N)]

# check_order[i]: i번째 톱니바퀴를 회전시킬 때 회전하는지 확인해봐야 하는 톱니바퀴 순서쌍
check_order = [
    [[0, 1], [1, 2], [2, 3]],
    [[1, 0], [1, 2], [2, 3]],
    [[2, 1], [2, 3], [1, 0]],
    [[3, 2], [2, 1], [1, 0]]
]

K = int(input())

for _ in range(K):
    # 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향
    # 1은 시계방향, -1은 반시계 방향
    n, d = map(int, input().split())
    n -= 1

    will_rotate = [0] * N
    will_rotate[n] = d

    # 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면,
    # B는 A가 회전한 방향과 반대방향으로 회전하게 된다
    for now, nxt in check_order[n]:
        # now의 2번과 nxt의 6번 확인
        if now < nxt:
            if lst[now][2] != lst[nxt][6]:
                will_rotate[nxt] = will_rotate[now] * -1
        # now의 6번과 nxt의 2번 확인
        else:
            if lst[now][6] != lst[nxt][2]:
                will_rotate[nxt] = will_rotate[now] * -1

    for n in range(N):
        if will_rotate[n] == 1:
            lst[n] = lst[n][-1] + lst[n][:-1]
        elif will_rotate[n] == -1:
            lst[n] = lst[n][1:] + lst[n][0]

# 각 톱니바퀴의 12시 방향이 S극(1)인지 여부
result = 0
for n in range(N):
    if lst[n][0] == '1':
        result += 2 ** n
print(result)