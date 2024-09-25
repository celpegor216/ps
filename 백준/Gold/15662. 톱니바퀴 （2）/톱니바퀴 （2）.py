N = int(input())
lst = [input() for _ in range(N)]

Q = int(input())
for _ in range(Q):
    idx, direction = map(int, input().split())
    idx -= 1

    rotates = [0] * N
    rotates[idx] = direction

    # 왼쪽으로 확인하기
    now = idx
    while now > 0 and lst[now][6] != lst[now - 1][2]:
        rotates[now - 1] = rotates[now] * -1
        now -= 1

    # 오른쪽으로 확인하기
    now = idx
    while now < N - 1 and lst[now][2] != lst[now + 1][6]:
        rotates[now + 1] = rotates[now] * -1
        now += 1

    for n in range(N):
        if rotates[n] == 1:
            lst[n] = lst[n][-1] + lst[n][:-1]
        elif rotates[n] == -1:
            lst[n] = lst[n][1:] + lst[n][0]


result = 0
for n in range(N):
    if lst[n][0] == '1':
        result += 1
print(result)