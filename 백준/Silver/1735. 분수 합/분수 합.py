A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

A = A1 * B2 + B1 * A2
B = B1 * B2

a, b = A, B
while b:
    a, b = b, a % b

print(A // a, B // a)