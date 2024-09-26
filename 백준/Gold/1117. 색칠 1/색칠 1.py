M, N, C, R, l, u, r, d = map(int, input().split())

a = (d - u) * (r - l)
b = (d - u) * (min(C, M - C, r) - l)

if b < 0:
    b = 0

print(N * M - (a + b) * (R + 1))