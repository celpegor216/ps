N, A, B = map(int, input().split())


def find():
    q = [N]
    used = [0] * (N + 1)
    used[N] = 1

    result = 0
    while q:
        nq = []

        for now in q:
            if now == 0:
                return result
            now -= 1

            for nxt in (now, now - A, now - B):
                if nxt >= 0 and not used[nxt]:
                    used[nxt] = 1
                    nq.append(nxt)
        
        q = nq
        result += 1


print(find())