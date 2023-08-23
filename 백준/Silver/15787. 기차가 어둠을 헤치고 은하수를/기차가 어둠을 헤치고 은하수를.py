N, M = map(int, input().split())
trains = [0 for _ in range(N + 1)]

for m in range(M):
    tmp = input()
    
    if tmp[0] == '1':
        command, i, x = map(int, tmp.split())
        trains[i] |= (1 << (x - 1))
    elif tmp[0] == '2':
        command, i, x = map(int, tmp.split())
        train = trains[i]
        if 2 ** (x - 1) <= train and bin(train)[-x] == '1':
            trains[i] -= 2 ** (x - 1)
    elif tmp[0] == '3':
        command, i = map(int, tmp.split())
        trains[i] <<= 1
        train = trains[i]
        if 2 ** 20 <= train and bin(train)[-21] == '1':
            trains[i] -= 2 ** 20
    elif tmp[0] == '4':
        command, i = map(int, tmp.split())
        trains[i] >>= 1

used = []
cnt = 0
for train in trains[1:]:
    if train not in used:
        used.append(train)
        cnt += 1

print(cnt)