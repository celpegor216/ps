N, K = map(int, input().split())

def find():
    q = [0]
    used = [0] * (N + 1)
    used[0] = 1

    k = 1
    while q and k <= K:
        nq = []

        for now in q:
            for nxt in (now + 1, now + now // 2):
                if nxt > N or used[nxt]:
                    continue

                used[nxt] = 1
                nq.append(nxt)

        q = nq
        k += 1

    return 'water' if not used[-1] else 'minigimbob'

print(find())