from collections import deque

T = input()
bucket = [0] * 26
for t in T:
    bucket[ord(t) - ord('A')] += 1

N = int(input())
books = []
for _ in range(N):
    cost, book = input().split()
    cost = int(cost)
    books.append((cost, book))

books.sort()

result = 21e8

q = deque()
q.append(('', 0, 0))

while q:
    nowt, nowi, nowc = q.popleft()

    if nowc >= result:
        continue

    flag = 0
    for i in range(26):
        if nowt.count(chr(ord('A') + i)) < bucket[i]:
            flag = 1
            break
    if not flag:
        result = nowc
        continue

    for i in range(nowi, N):
        q.append((nowt + books[i][1], i + 1, nowc + books[i][0]))

if result == 21e8:
    print(-1)
else:
    print(result)