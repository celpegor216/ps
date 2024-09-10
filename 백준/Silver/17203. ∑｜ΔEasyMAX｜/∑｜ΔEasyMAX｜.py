N, Q = map(int, input().split())
lst = list(map(int, input().split()))
acc_sum = [0] * N

for n in range(1, N):
    acc_sum[n] = acc_sum[n - 1] + abs(lst[n] - lst[n - 1])

for _ in range(Q):
    s, e = map(int, input().split())

    print(acc_sum[e - 1] - acc_sum[s - 1])