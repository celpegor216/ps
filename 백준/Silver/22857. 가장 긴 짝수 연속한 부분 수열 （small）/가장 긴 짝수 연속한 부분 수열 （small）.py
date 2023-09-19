N, K = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
now = 0
cnt = 0
cnt_k = 0

for n in range(N):
    while now < N and cnt_k <= K:
        if lst[now] % 2:
            cnt_k += 1
        else:
            cnt += 1
    
        now += 1
    
    result = max(result, cnt)

    if lst[n] % 2:
        cnt_k -= 1
    else:
        cnt -= 1

print(result)