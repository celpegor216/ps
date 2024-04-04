N, L = map(int, input().split())
lst = sorted(map(int, input().split()))

result = 1
now = lst[0]

for n in range(1, N):
    if lst[n] + 1 > now + L:
        result += 1
        now = lst[n]

print(result)