N = int(input())
lst = list(map(int, input().split()))

result = 0

# 커지는 것 찾기
cnt = 1
for n in range(1, N):
    if lst[n] >= lst[n - 1]:
        cnt += 1
    else:
        result = max(result, cnt)
        cnt = 1
result = max(result, cnt)

# 작아지는 것 찾기
cnt = 1
for n in range(1, N):
    if lst[n] <= lst[n - 1]:
        cnt += 1
    else:
        result = max(result, cnt)
        cnt = 1
result = max(result, cnt)

print(result)