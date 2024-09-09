A, B = map(int, input().split())
N = int(input())
lst = list(map(int, input().split()))

A_to_10 = 0

for n in range(N):
    A_to_10 += lst[n] * (A ** (N - n - 1))

result = []

while A_to_10:
    result.append(A_to_10 % B)
    A_to_10 //= B

print(*result[::-1])