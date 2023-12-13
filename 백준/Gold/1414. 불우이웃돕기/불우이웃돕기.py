import heapq

N = int(input())
q = []

result = 0

for n in range(N):
    s = input()

    for m in range(N):
        if 'a' <= s[m] <= 'z':
            if n != m:
                heapq.heappush(q, (ord(s[m]) - ord('a') + 1, n, m))
            result += ord(s[m]) - ord('a') + 1
        elif 'A' <= s[m] <= 'Z':
            if n != m:
                heapq.heappush(q, (ord(s[m]) - ord('A') + 26 + 1, n, m))
            result += ord(s[m]) - ord('A') + 26 + 1

groups = [x for x in range(N)]

def find(a):
    if groups[a] != a:
        groups[a] = find(groups[a])
    return groups[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        groups[group_b] = group_a
        return 1
    return 0

while q:
    cost, a, b = heapq.heappop(q)

    result -= union(a, b) * cost

flag = 0
g = find(groups[0])
for i in range(1, N):
    if find(groups[i]) != g:
        flag = 1
        break

if N > 1 and flag:
    print(-1)
else:
    print(result)