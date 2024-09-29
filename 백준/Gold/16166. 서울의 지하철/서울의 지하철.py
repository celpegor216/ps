N = int(input())
stations = dict()
lines = []
for n in range(N):
    K, *tmp = map(int, input().split())

    if K != 1 and tmp[0] == tmp[-1]:
        tmp.pop()

    lines.append(tmp)
    for item in tmp:
        if not stations.get(item):
            stations[item] = []
        stations[item].append(n)
E = int(input())
    

def find():
    q = [0]
    results = dict()
    results[0] = 1

    if not stations.get(0):
        return 0

    for line in stations[0]:
        for nxt in lines[line]:
            results[nxt] = 1
            q.append(nxt)

    while q:
        nq = []

        for now in q:
            if now == E:
                return results[now]
            
            for line in stations[now]:
                for nxt in lines[line]:
                    if results.get(nxt):
                        continue
                        
                    results[nxt] = results[now] + 1
                    nq.append(nxt)

        q = nq

    return 0


print(find() - 1)