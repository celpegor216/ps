import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
lst = list(map(int, input().split()))
head = 0

for _ in range(Q):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        lst[(head + cmd[1] - 1) % N] += cmd[2]
    elif cmd[0] == 2:
        head = (head - cmd[1]) % N
    elif cmd[0] == 3:
        head = (head + cmd[1]) % N

lst = lst[head:] + lst[:head]
print(*lst)