import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = []

for i in range(4):
    lst.sort(key=lambda x: (-x[i + 1], x[0]))

    idx = 0
    while 1:
        if lst[idx][0] not in result:
            result.append(lst[idx][0])
            break
        idx += 1

print(*result)