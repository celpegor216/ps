S, N, M = map(int, input().split())
U = 0

for _ in range(N + M):
    cmd = int(input())

    if cmd == 1:
        U += 1
        if U > S:
            S *= 2
    else:
        U -= 1

print(S)