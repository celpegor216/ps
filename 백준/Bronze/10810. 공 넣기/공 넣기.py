N, M = map(int, input().split())
bucket = [0] * (N + 1)


for _ in range(M):
    i, j, k = map(int, input().split())

    for n in range(i, j + 1):
        bucket[n] = k

print(*bucket[1:])