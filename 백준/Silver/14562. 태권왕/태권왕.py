TC = int(input())

def find():
    S, T = map(int, input().split())

    q = [(S, T)]
    used = set()
    used.add((S, T))

    result = 0
    while q:
        nq = []

        for s, t in q:
            if s == t:
                return result
            
            if (s + 1, t) not in used:
                used.add((s + 1, t))
                nq.append((s + 1, t))
            if s * 2 <= t + 3 and (s * 2, t + 3) not in used:
                used.add((s * 2, t + 3))
                nq.append((s * 2, t + 3))

        q = nq
        result += 1

for _ in range(TC):
    print(find())