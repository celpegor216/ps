N = 100
board = [x for x in range(N + 1)]

L, S = map(int, input().split())

for _ in range(L + S):
    x, y = map(int, input().split())
    board[x] = y


def find(start):
    used = [0] * (N + 1)
    used[start] = 1

    q = [start]

    result = 0
    while q:
        nq = []

        for now in q:
            if now == N:
                return result

            for i in range(1, 7):
                nxt = now + i
                if nxt > N:
                    continue
                nxt = board[nxt]

                if used[nxt]:
                    continue
                    
                used[nxt] = 1
                nq.append(nxt)
        
        q = nq
        result += 1
    

print(find(1))