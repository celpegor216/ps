N, W = map(int, input().split())

lst = [0] * (N + 1)

for n in range(N - 1):
    a, b = map(int, input().split())
    lst[a] += 1
    lst[b] += 1

result = 0
for n in range(2, N + 1):
    if lst[n] == 1:
        result += 1

print(W / result)