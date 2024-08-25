N = int(input())
lst = list(map(int, input().split()))

result = 0
cnt = 0
for i in range(N):
    if lst[i]:
        cnt += 1
        result = max(result, cnt)
    else:
        cnt = 0

print(result)