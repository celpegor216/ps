M = int(input())
N = int(input())
order = input()

lines = [input() for _ in range(N)]

up = [''] * M

for m in range(M):
    now = m
    
    for n in range(N):
        if lines[n][0] == '?':
            up[now] = chr(ord('A') + m)
            break

        if now < M - 1 and lines[n][now] == '-':
            now += 1
        elif now and lines[n][now - 1] == '-':
            now -= 1

down = [m for m in range(M)]

for m in range(M):
    now = m
    
    for n in range(N - 1, -1, -1):
        if lines[n][0] == '?':
            down[now] = m
            break

        if now < M - 1 and lines[n][now] == '-':
            now += 1
        elif now and lines[n][now - 1] == '-':
            now -= 1

result = ['*'] * (M - 1)

m = 0
while m < M - 1:
    if order[down[m]] != up[m]:
        if order[down[m]] == up[m + 1] and order[down[m + 1]] == up[m]:
            result[m] = '-'
            m += 1
        else:
            result = ['x'] * (M - 1)
            break
    m += 1

print(''.join(result))