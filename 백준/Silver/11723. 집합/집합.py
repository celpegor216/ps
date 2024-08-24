import sys
input = sys.stdin.readline

M = int(input())

S = [0] * 21

for _ in range(M):
    cmd = input().split()

    if cmd[0] == 'add':
        S[int(cmd[1])] = 1
    elif cmd[0] == 'remove':
        S[int(cmd[1])] = 0
    elif cmd[0] == 'check':
        print(S[int(cmd[1])])
    elif cmd[0] == 'toggle':
        S[int(cmd[1])] ^= 1
    elif cmd[0] == 'all':
        S = [1] * 21
    elif cmd[0] == 'empty':
        S = [0] * 21