N = int(input())
lst = list(map(int, input().split()))

maxK = 0

for i in range(2, 12):
    if 2 ** i > N:
        maxK = i
        break

def fill(tmp):
    res = []

    for k in range(1, maxK):
        middle = N - 2 ** k
        now = tmp[middle:] + tmp[:middle]

        for i in range(k):
            start = 2 ** (k - i - 1)
            end = 2 ** (k - i)
            now = now[start:end] + now[:start] + now[end:]
        
        res.append(now)

    return res

res1 = fill([x for x in range(1, N + 1)])
res2 = [fill(item) for item in res1]

result = []

for i in range(len(res2)):
    if result:
        break

    for j in range(len(res2[i])):
        if res2[i][j] == lst:
            result = [i + 1, j + 1]
            break

print(*result)