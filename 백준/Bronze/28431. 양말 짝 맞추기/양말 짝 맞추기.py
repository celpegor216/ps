N = 5
M = 10
bucket = [0] * M

for _ in range(N):
    bucket[int(input())] += 1

for i in range(M):
    if bucket[i] % 2:
        print(i)
        break