from collections import deque


A, B = map(int, input().split())

q = deque()
used = set()

q.append(A)
used.add(A)

def find():
    result = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()

            if now == B:
                return result

            for nxt in (now + 1, now * 2):
                if nxt not in used and nxt <= B:
                    used.add(nxt)
                    q.append(nxt)

        result += 1

print(find())