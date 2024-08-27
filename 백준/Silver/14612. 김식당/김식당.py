N, M = map(int, input().split())
# tables[i]: i번째 테이블이 음식을 주문한 시간
tables = [0] * (M + 1)
# 포스트잇 정렬 순서
order = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'order':
        m, t = map(int, cmd[1:])
        tables[m] = t
        order.append(m)
    elif cmd[0] == 'sort':
        order.sort(key=lambda x: (tables[x], x))
    else:
        m = int(cmd[1])
        tables[m] = 0
        order.remove(m)

    if order:
        print(*order)
    else:
        print('sleep')