import sys
input = sys.stdin.readline


N, K = map(int, input().split())
lst = [float(input()) for _ in range(N)]

lst.sort()

total = sum(lst[K:N - K])

print(f'{(total / (N - K * 2)) + 0.00000001:0.2f}')
print(f'{((total + lst[K] * K + lst[N - K - 1] * K) / N) + 0.00000001:0.2f}')