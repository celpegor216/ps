# 팀원 아이디어 따라서 구현

N, M = map(int, input().split())
folders = dict()

for _ in range(N + M):
    P, F, C = input().split()
    folders[P] = folders.get(P, []) + [F]
    if C == '1' and not folders.get(F):
        folders[F] = []

K = int(input())
for _ in range(K):
    a, b = input().split()
    a = a.split('/')[-1]
    b = b.split('/')[-1]

    while folders[a]:
        item = folders[a].pop()
        if item not in folders[b]:
            folders[b].append(item)

memo = dict()
def dfs(now):
    files = []
    for child in folders[now]:
        if child in folders.keys():    # 폴더인 경우
            files += dfs(child)
        else:
            files.append(child)
    
    memo[now] = [len(set(files)), len(files)]
    return files

dfs('main')

Q = int(input())
for _ in range(Q):
    print(*memo[input().split('/')[-1]])