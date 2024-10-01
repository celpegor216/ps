TC = int(input())

MAX = 10 ** 4
LEFT = 10 ** 3

def find():
    used = [0] * MAX
    used[A] = 1

    q = [(A, '')]

    while q:
        nq = []

        for now, path in q:
            if now == B:
                return path

            # D
            nxt = (now * 2) % MAX
            if not used[nxt]:
                used[nxt] = 1
                nq.append((nxt, path + 'D'))

            # S
            nxt = (now - 1) % MAX
            if not used[nxt]:
                used[nxt] = 1
                nq.append((nxt, path + 'S'))

            # L
            nxt = (now % LEFT) * 10 + now // LEFT
            if not used[nxt]:
                used[nxt] = 1
                nq.append((nxt, path + 'L'))

            # R
            nxt = (now % 10) * LEFT + now // 10
            if not used[nxt]:
                used[nxt] = 1
                nq.append((nxt, path + 'R'))

        q = nq


for _ in range(TC):
    A, B = map(int, input().split())

    print(find())