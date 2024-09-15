from collections import deque

N = int(input())
lst = list(map(int, input().split()))
s, e = map(lambda x: int(x) - 1, input().split())

def find():
    q = deque()
    q.append(s)

    used = [0] * N
    used[s] = 1

    result = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()

            if now == e:
                return result
            
            for d in (lst[now], -lst[now]):
                nxt = now + d
                while 0 <= nxt < N:
                    if not used[nxt]:
                        used[nxt] = 1
                        q.append(nxt)
                    nxt += d

        result += 1

    return -1

print(find())