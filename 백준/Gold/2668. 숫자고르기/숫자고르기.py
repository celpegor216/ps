N = int(input())
lst = [0] + [int(input()) for _ in range(N)]

result = set()

for n in range(1, N + 1):
    flag = 0
    nxt = lst[n]
    tmp = []
    while nxt not in tmp:
        if nxt in result:
            flag = 1
            break
        tmp.append(nxt)
        nxt = lst[nxt]

    if not flag and tmp[-1] == n:
        result = result.union(set(tmp))

print(len(result))
for item in sorted(result):
    print(item)