T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

dic_a = dict()

for i in range(N):
    total = 0
    for j in range(i, N):
        total += A[j]
        dic_a[total] = dic_a.get(total, 0) + 1

dic_b = dict()

for i in range(M):
    total = 0
    for j in range(i, M):
        total += B[j]
        dic_b[total] = dic_b.get(total, 0) + 1

result = 0

for key in dic_a:
    target = T - key
    result += dic_a[key] * dic_b.get(target, 0)

print(result)