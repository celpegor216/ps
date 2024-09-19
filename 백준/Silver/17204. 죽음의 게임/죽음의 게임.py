N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

used = [0] * N

now = 0
cnt = 0
result = -1
while 1:
    if used[now]:
        break
    elif now == K:
        result = cnt
        break

    used[now] = 1
    now = lst[now]
    cnt += 1

print(result)