N = int(input())
lst = [int(input()) for _ in range(N)]

lcs = [1] * N

for n in range(1, N):
    for i in range(n):
        if lst[i] < lst[n]:
            lcs[n] = max(lcs[n], lcs[i] + 1)

print(N - max(lcs))