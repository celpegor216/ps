N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x: (-x[1], -x[2], -x[3]))

result = [0] * (N + 1)

before = 0
def check(a, b, c):
    if a < lst[before][1]:
        return 1
    if b < lst[before][2]:
        return 1
    if c < lst[before][3]:
        return 1
    return 0

for n in range(N):
    if n == 0 or check(*lst[n][1:]):
        result[lst[n][0]] = n + 1
        before = n
    else:
        result[lst[n][0]] = result[lst[before][0]]

print(result[K])