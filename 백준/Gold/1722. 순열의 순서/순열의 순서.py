N = int(input())
cmd = list(map(int, input().split()))

cnts = [1]
for n in range(1, N):
    cnts.append(cnts[-1] * n)
cnts = cnts[::-1]

if cmd[0] == 1:
    k = cmd[1]
    result = []
    left = [n for n in range(1, N + 1)]
    for n in range(N):
        for item in left:
            if k <= cnts[n]:
                result.append(item)
                left.remove(item)
                break
            else:
                k -= cnts[n]
    print(*result)
else:
    result = 1
    left = [n for n in range(1, N + 1)]
    for n in range(N):
        idx = left.index(cmd[n + 1])
        left.remove(cmd[n + 1])
        result += cnts[n] * idx
    print(result)