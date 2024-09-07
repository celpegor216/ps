N, M = map(int, input().split())
lst = [input() for _ in range(N)]

dic = {'-': '|', '|': '-', '/': '\\', '\\': '/', '^': '<', '<': 'v', 'v': '>', '>': '^'}

result = [[''] * N for _ in range(M)]

for m in range(M):
    origin_m = M - m - 1
    for n in range(N):
        result[m][n] = dic.get(lst[n][origin_m], lst[n][origin_m])

    print(''.join(result[m]))