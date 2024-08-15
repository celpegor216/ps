N = int(input())
lst = [int(input()) for _ in range(N)]

A = lst[1] - lst[0]
for n in range(2, N):
    a, b = A, lst[n] - lst[n - 1]
    while b:
        a, b = b, a % b
    A = a

result = 0
for n in range(1, N):
    result += (lst[n] - lst[n - 1] - 1) // A

print(result)