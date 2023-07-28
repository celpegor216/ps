N, S = map(int, input().split())
lst = [int(input()) for _ in range(N)]

lst.sort()

total = 0
half = S / 2

for i in range(N):
    if lst[i] > half:
        break
    for j in range(i + 1, N):
        if lst[i] + lst[j]> S:
            break
        total += 1

print(total)