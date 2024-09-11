import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int, input().split()))
is_opened = [1] * N

total = sum(lst)
print(total)

Q = int(input())
for _ in range(Q):
    cmd = list(map(int, input().split()))
    idx = cmd[1] - 1

    if cmd[0] == 1:
        if is_opened[idx]:
            total -= lst[idx]
            lst[idx] = cmd[2]
            total += cmd[2]
        else:
            lst[idx] = cmd[2]
    else:
        if is_opened[idx]:
            total -= lst[idx]
            is_opened[idx] = 0
        else:
            total += lst[idx]
            is_opened[idx] = 1

    print(total)