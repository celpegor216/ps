N, K = map(int, input().split())

lst = [x for x in range(N + 1)]

result = []

last = 0

for n in range(N):
    cnt = 0
    idx = last

    while 1:
        if lst[idx] > 0:
            cnt += 1
            if cnt == K:
                break

        idx += 1
        if idx == N + 1:
            idx = 0

    last = idx
    lst[last] = 0
    result.append(last)

print('<', end='')
for i in range(N):
    if i != N - 1:
        print(result[i], end=', ')
    else:
        print(result[i], end='>')
