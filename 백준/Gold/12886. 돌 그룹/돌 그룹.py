lst = list(map(int, input().split()))


def find():
    q = [lst]
    used = set()
    used.add(tuple(lst))

    while q:
        nq = []

        for now in q:
            if now[0] == now[1] == now[2]:
                return 1

            for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
                if now[i] != now[j]:
                    nxt = sorted((now[i], now[j]))
                    nxt[0], nxt[1] = nxt[0] * 2, nxt[1] - nxt[0]
                    if nxt[1] < 0:
                        continue

                    nxt.append(now[k])
                    nxt.sort()
                    tup = tuple(nxt)

                    if tup not in used:
                        used.add(tup)
                        nq.append(nxt)

        q = nq

    return 0


print(find())
