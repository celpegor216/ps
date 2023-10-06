N, K = map(int, input().split())
minv = K * (K + 1) / 2

if minv > N:
    print(-1)
elif not (N - minv) % K:
    print(K - 1)
else:
    print(K)