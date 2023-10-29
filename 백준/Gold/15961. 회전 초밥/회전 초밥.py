import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]

used = [0] * (D + 1)
used[C] = 1

cnt = 1
result = 1

for k in range(K):
    if used[lst[k]] == 0:
        cnt += 1
    
    used[lst[k]] += 1

for n in range(N):
    result = max(result, cnt)

    used[lst[n]] -= 1
    if used[lst[n]] == 0:
        cnt -= 1
    
    if used[lst[(n + K) % N]] == 0:
        cnt += 1
    used[lst[(n + K) % N]] += 1

print(result)