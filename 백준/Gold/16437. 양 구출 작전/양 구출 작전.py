from collections import deque

N = int(input())
lst = [0] * (N)
children = [0] * N
parents = [0] * N

for n in range(1, N):
    t, a, p = input().split()
    a = int(a)
    p = int(p) - 1

    if t == 'S':
        lst[n] += a
    else:
        lst[n] -= a
    
    children[p] += 1
    parents[n] = p

q = deque()

for n in range(N):
    if not children[n]:
        q.append(n)

while q:
    now = q.popleft()

    if now == 0:
        break
    
    parent = parents[now]

    if lst[now] > 0:
        lst[parent] += lst[now]

    children[parent] -= 1
    if not children[parent]:
        q.append(parent)

print(lst[0])