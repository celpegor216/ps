X = int(input())
S = input()
N = len(S)

used = [S]
now = S

while 1:
    nxt = ''
    head = 0
    tail = N - 1

    while head <= tail:
        nxt += now[head] + now[tail]
        head += 1
        tail -= 1

    if N % 2:
        nxt = nxt[:-1]

    if nxt in used:
        break

    used.append(nxt)
    now = nxt

print(used[-X % len(used)])