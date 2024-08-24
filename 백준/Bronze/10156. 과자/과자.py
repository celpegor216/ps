K, N, M = map(int, input().split())
print(K * N - M if K * N > M else 0)