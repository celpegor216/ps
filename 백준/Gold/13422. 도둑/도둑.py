T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 0
    total = sum(lst[:M])

    if N == M:
        if total < K:
            cnt += 1
        print(cnt)
    else:
        for n in range(N):
            if total < K:
                cnt += 1

            total -= lst[n]
            total += lst[(n + M) % N]
        
        print(cnt)