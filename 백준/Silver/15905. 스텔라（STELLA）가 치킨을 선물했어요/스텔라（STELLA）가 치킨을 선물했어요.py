N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x: (-x[0], x[1]))

result = 0
for i in range(5, N):
    if lst[i][0] == lst[4][0]:
        result += 1
    else:
        break

print(result)