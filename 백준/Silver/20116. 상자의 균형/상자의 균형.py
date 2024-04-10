N, L = map(int, input().split())
lst = list(map(int, input().split()))

now = 0
cnt = 0

result = "stable"

for n in range(N - 1, 0, -1):
    now += lst[n]
    cnt += 1
    avg = now / cnt

    if not (lst[n - 1] - L < avg < lst[n - 1] + L):
        result = "un" + result
        break

print(result)