from collections import deque

A, B, C = map(int, input().split())

used = set()
used.add((0, 0, C))

q = deque()
q.append((0, 0, C))

def check(a, b, c):
    if (a, b, c) not in used:
        used.add((a, b, c))
        q.append((a, b, c))

while q:
    a, b, c = q.popleft()

    # a > b
    if a + b <= B:
        check(0, a + b, c)
    else:
        diff = B - b
        check(a - diff, B, c)

    # a > c
    if a + c <= C:
        check(0, b, a + c)
    else:
        diff = C - c
        check(a - diff, b, C)

    # b > a
    if a + b <= A:
        check(a + b, 0, c)
    else:
        diff = A - a
        check(A, b - diff, c)

    # b > c
    if b + c <= C:
        check(a, 0, b + c)
    else:
        diff = C - c
        check(a, b - diff, C)

    # c > a
    if a + c <= A:
        check(a + c, b, 0)
    else:
        diff = A - a
        check(A, b, c - diff)

    # c > b
    if b + c <= B:
        check(a, b + c, 0)
    else:
        diff = B - b
        check(a, B, c - diff)

used = sorted(set([x[2] for x in sorted(used, key=lambda x: x[2]) if not x[0]]))

print(*used)