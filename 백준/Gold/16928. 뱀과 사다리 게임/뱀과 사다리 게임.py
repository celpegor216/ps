from collections import deque


N, M = map(int, input().split())
MAX = 100
board = [n for n in range(MAX + 1)]

for _ in range(N + M):
    a, b = map(int, input().split())
    board[a] = b

def find():
    q = deque()
    q.append(1)

    used = [0] * (MAX + 1)
    used[1] = 1

    result = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()

            if now == MAX:
                return result

            for i in range(1, 7):
                nxt = now + i
                if nxt <= MAX and not used[nxt]:
                    used[nxt] = 1
                    q.append(board[nxt])

        result += 1

print(find())