N = int(input())
lst = list(map(int, input().split()))

result = []

for n in range(N - 1, 0, -1):
    if lst[n - 1] > lst[n]:
        tmp = lst[n - 1:]

        # tmp에서 lst[n - 1]보다 작은 것들 중에 가장 큰 수
        t = max([x for x in tmp if x < lst[n - 1]])
        tmp.remove(t)

        result = lst[:n - 1] + [t] + sorted(tmp, reverse=True)
        break

if result:
    print(*result)
else:
    print(-1)