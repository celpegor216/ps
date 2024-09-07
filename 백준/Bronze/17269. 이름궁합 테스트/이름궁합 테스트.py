cnts = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1,]

N, M = map(int, input().split())
A, B = input().split()

result = []
for i in range(min(N, M)):
    result.append(cnts[ord(A[i]) - ord('A')])
    result.append(cnts[ord(B[i]) - ord('A')])

if N > M:
    for i in range(M, N):
        result.append(cnts[ord(A[i]) - ord('A')])
elif N < M:
    for i in range(N, M):
        result.append(cnts[ord(B[i]) - ord('A')])

for i in range(N + M - 2 , 0, -1):
    res = []
    for j in range(i + 1):
        res.append((result[j] + result[j + 1]) % 10)
    
    result = res

print(f'{res[0] * 10 + res[1]}%')