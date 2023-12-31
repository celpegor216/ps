A, B = input().split()
N, M = len(A), len(B)

result = 50

for i in range(M - N + 1):
    tmp = 0

    for n in range(N):
        if A[n] != B[i + n]:
            tmp += 1
    
    if tmp < result:
        result = tmp

print(result)