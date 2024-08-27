N, K = map(int, input().split())
lst = [''] * N

# 현재 lst에서 화살표가 가리키고 있는 글자의 위치
now = 0
for _ in range(K):
    move, char = input().split()

    # 화살표가 가리키는 글자가 몇 번 바뀌었는지 == 몇 칸 움직였는지
    move = int(move)

    # 바퀴가 시계방향으로 돌아감 > 화살표는 시계반대방향으로 가야함
    now = (now - move) % N

    # > 바퀴에 같은 글자는 두 번 이상 등장하지 않음
    if not lst[now] and char not in lst:
        lst[now] = char
    elif lst[now] == char:
        continue
    else:
        print('!')
        break
else:
    for n in range(N):
        # 출력할 때는 화살표에서부터 시계방향으로 움직여야 함
        idx = (now + n) % N
        print(lst[idx] if lst[idx] else '?', end='')