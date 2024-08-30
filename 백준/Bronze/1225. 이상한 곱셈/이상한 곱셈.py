A, B = map(lambda x: list(map(int, x)), input().split())

result = 0
for i in range(len(A)):
    for j in range(len(B)):
        result += A[i] * B[j]

print(result)