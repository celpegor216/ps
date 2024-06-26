N = int(input())
lst = list(map(int, input().split()))

result = 0

for n in range(N):
    if lst[n - 1] >= lst[n]:
        result += 1

print(result)