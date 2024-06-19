N = int(input())

flat = [0]
volume = [0]

M = 0
while volume[-1] < N:
    M += 1
    flat.append(M + flat[-1])
    volume.append(flat[-1] + volume[-1])

result = 0

before = [21e8] * (N + 1)
now = [21e8] * (N + 1)

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if j < volume[i]:
            now[j] = before[j]
        elif j == volume[i]:
            now[j] = 1
        else:
            now[j] = min(before[j], now[j - volume[i]] + 1)
        
    before = now[:]
    now = [21e8] * (N + 1)


print(before[-1])