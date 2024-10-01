import sys
input = sys.stdin.readline


N = int(input())

lst = []
for n in range(N):
    c, s = map(int, input().split())
    lst.append((s, c, n))

lst.sort()

total = 0
colors_total = dict()
now_size = 0
tmp_total = dict()

result = [0] * N
for s, c, n in lst:
    if now_size != s:
        for key, value in tmp_total.items():
            colors_total[key] = colors_total.get(key, 0) + value
            total += value
        now_size = s
        tmp_total = dict()

    result[n] = total - colors_total.get(c, 0)
    tmp_total[c] = tmp_total.get(c, 0) + s

for item in result:
    print(item)