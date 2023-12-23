N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)

result = 0

for n in range(N):
    result += A[n] * B[n]

print(result)