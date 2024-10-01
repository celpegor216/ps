N = int(input())

def find():
    q = [N]
    used = dict()
    used[N] = 1

    while q:
        nq = []

        for now in q:
            if now == 1:
                return used[now] - 1

            if not now % 3 and not used.get(now // 3):
                used[now // 3] = used[now] + 1
                nq.append(now // 3)

            if not now % 2 and not used.get(now // 2):
                used[now // 2] = used[now] + 1
                nq.append(now // 2)

            if not used.get(now - 1):
                used[now - 1] = used[now] + 1
                nq.append(now - 1)

        q = nq


print(find())