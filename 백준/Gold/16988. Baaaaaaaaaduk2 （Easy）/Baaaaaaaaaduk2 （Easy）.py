from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

used = [[0] * M for _ in range(N)]

pairs = dict()
result = 0

for n in range(N):
    for m in range(M):
        if not used[n][m] and lst[n][m] == 2:
            used[n][m] = 1
            
            q = deque()
            q.append((n, m))

            cnt = 0
            zeros = set()

            while q:
                cnt += 1
                y, x = q.popleft()

                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                        if lst[ny][nx] == 0:
                            zeros.add((ny, nx))
                        elif lst[ny][nx] == 2:
                            used[ny][nx] = 1
                            q.append((ny, nx))

            if len(zeros) <= 2:
                zeros = sorted(zeros)
                key = str(len(zeros)) + str(zeros)
                if pairs.get(key):
                    pairs[key] += cnt
                else:
                    pairs[key] = cnt

result = 0

one = dict()
two = dict()

for key in pairs.keys():
    if key[0] == '1':
        one[key] = pairs[key]
    else:
        two[key] = pairs[key]

for key in one.keys():
    for key2 in two.keys():
        if key[2:len(key) - 1] in key2:
            two[key2] += one[key]

result = 0
if pairs:
    if one:
        result = sum(sorted(one.values(), reverse=True)[:2])
    if two:
        result = max(result, max(two.values()))

print(result)