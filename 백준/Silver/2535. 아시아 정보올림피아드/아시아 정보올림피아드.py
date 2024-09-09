N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x: -x[2])

results = []
countries = []

for n in range(N):
    if countries.count(lst[n][0]) > 1:
        continue

    results.append(lst[n][:2])
    countries.append(lst[n][0])

    if len(results) == 3:
        break

for result in results:
    print(*result)