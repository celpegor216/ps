N, M, Q = map(int, input().split())
middle = [list(map(int, input().split())) for _ in range(M)]
last = list(map(int, input().split()))

total_bias = last[-1]
multiples = [0] * N
for m in range(M):
    C = middle[m][0]
    for i in range(1, C + 1):
        multiples[middle[m][i] - 1] += middle[m][i + C] * last[m]
    total_bias += middle[m][-1] * last[m]


for _ in range(Q):
    first = list(map(int, input().split()))

    result = total_bias
    for n in range(N):
        result += first[n] * multiples[n]

    print(result)