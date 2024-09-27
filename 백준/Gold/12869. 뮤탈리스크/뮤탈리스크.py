_ = int(input())
N = 3
lst = list(map(int, input().split()))
while len(lst) < 3:
    lst.append(0)


def find():
    q = [lst]
    used = set()
    used.add(tuple(lst))

    result = 0
    while q:
        nq = []

        for now in q:
            if not sum(now):
                return result

            for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)):
                nxt = now[:]

                nxt[i] = max(0, nxt[i] - 9)
                nxt[j] = max(0, nxt[j] - 3)
                nxt[k] = max(0, nxt[k] - 1)

                tup = tuple(nxt)

                if tup not in used:
                    used.add(tup)
                    nq.append(nxt)

        q = nq
        result += 1

print(find())