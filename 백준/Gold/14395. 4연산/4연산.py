S, T = map(int, input().split())


def find():
    if S == T:
        return 0

    q = [(S, '')]
    used = set()
    used.add(S)

    while q:
        nq = []

        for now, path in q:
            if now == T:
                return path

            for nxt, calc in ((now ** 2, '*'), (now * 2, '+'), (0, '-'), (1, '/')):
                if nxt in used or nxt > T:
                    continue

                used.add(nxt)
                nq.append((nxt, path + calc))

        q = nq

    return -1


print(find())
