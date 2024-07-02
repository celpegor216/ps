N, Q = map(int, input().split())
lst = list(map(int, input().split()))

for _ in range(Q):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        print(sum(lst[cmd[1] - 1:cmd[2]]))
        lst[cmd[1] - 1], lst[cmd[2] - 1] = lst[cmd[2] - 1], lst[cmd[1] - 1]
    else:
        print(sum(lst[cmd[1] - 1:cmd[2]]) - sum(lst[cmd[3] - 1:cmd[4]]))