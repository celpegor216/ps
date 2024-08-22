import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()

for _ in range(N):
    S = input().strip()

    if len(S) >= M:
        dic[S] = dic.get(S, 0) + 1

for key, value in sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(key)