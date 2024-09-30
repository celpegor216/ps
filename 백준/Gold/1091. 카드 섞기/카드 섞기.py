N = int(input())
targets = list(map(int, input().split()))
shuffles = list(map(int, input().split()))

used = set()

now = [n for n in range(N)]

result = -1
time = 0
while 1:
    for n in range(N):
        if n % 3 != targets[now[n]]:
            break
    else:
        result = time
        break

    nxt = [0] * N
    for n in range(N):
        nxt[shuffles[n]] = now[n]

    tup = tuple(nxt)
    if tup in used:
        break

    used.add(tup)
    now = nxt
    time += 1

print(result)