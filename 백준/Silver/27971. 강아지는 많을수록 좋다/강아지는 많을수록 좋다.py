N, M, A, B = map(int, input().split())

used = [0] * (N + 1)

for _ in range(M):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        used[i] = 1

def find():
    q = [0]

    result = 0

    while q:
        nq = []

        for now in q:

            if now == N:
                return result

            for nxt in (now + A, now + B):
                if nxt <= N and not used[nxt]:
                    nq.append(nxt)
                    used[nxt] = 1
        
        q = nq
        result += 1
    
    return -1


print(find())