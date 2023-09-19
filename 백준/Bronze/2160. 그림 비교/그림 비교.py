N = int(input())

lst = []

for n in range(N):
    tmp = [input() for _ in range(5)]
    lst.append(tmp)

result = 21e8
r1, r2 = -1, -1

for i in range(N - 1):
    for j in range(i + 1, N):
        total = 0

        for n in range(5):
            for m in range(7):
                if lst[i][n][m] != lst[j][n][m]:
                    total += 1
        
        if total < result:
            r1, r2 = i, j
            result = total

print(r1 + 1, r2 + 1)