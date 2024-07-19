N, M = map(int, input().split())
lst_N = list(map(int, input().split()))
lst_M = list(map(int, input().split()))

if N < M:
    lst_N += [0] * (M - N)
else:
    lst_M += [0] * (N - M)

for i in range(max(N, M)):
    lst_M[i] -= lst_N[i]

print(max(max(lst_M), 0))