import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_to_idx = dict()
idx_to_name = dict()

for n in range(1, N + 1):
    name = input().strip()
    name_to_idx[name] = n
    idx_to_name[n] = name

for _ in range(M):
    query = input().strip()

    if query.isdigit():
        print(idx_to_name[int(query)])
    else:
        print(name_to_idx[query])