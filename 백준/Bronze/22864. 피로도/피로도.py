A, B, C, M = map(int, input().split())

work = 0
tired = 0

for i in range(24):
    if tired + A <= M:
        work += B
        tired += A
    else:
        tired -= C
        if tired < 0:
            tired = 0

print(work)