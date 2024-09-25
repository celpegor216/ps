N = int(input())
lst = []

transform = lambda x: (ord(x[0]) - ord('A')) * 1000 + int(x[2:])

for _ in range(N):
    lst += list(map(transform, input().split()))

order = {value: idx for idx, value in enumerate(sorted(lst))}

waitings = []
now = 0
for num in lst:
    if order[num] > now:
        waitings.append(num)
    else:
        now += 1

    while waitings and order[waitings[-1]] == now:
        waitings.pop()
        now += 1


print('GOOD' if now == N * 5 else 'BAD')