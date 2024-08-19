N, A, B = map(int, input().split())

if A > B:
    A, B = B, A

result = 1

while not(A % 2 and A + 1 == B):
    if A % 2:
        A = A // 2 + 1
    else:
        A //= 2

    if B % 2:
        B = B // 2 + 1
    else:
        B //= 2

    result += 1

print(result)