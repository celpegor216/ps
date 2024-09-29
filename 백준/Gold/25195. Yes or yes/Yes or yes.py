import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)

used = [0] * (N + 1)

S = int(input())
tmp = list(map(int, input().split()))
for item in tmp:
    used[item] = 1


def find():
    if used[1]:
        return 'Yes'

    q = [1]
    used[1] = 1

    while q:
        nq = []

        for now in q:
            if not lst[now]:
                return 'yes'
            
            for nxt in lst[now]:
                if used[nxt]:
                    continue
                
                used[nxt] = 1
                nq.append(nxt)
        
        q = nq
    

    return 'Yes'


print(find())