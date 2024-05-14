# 시간 초과
# 해답: https://rapun7el.tistory.com/323

import sys
input = sys.stdin.readline

C, N = map(int, input().strip().split())
colors = dict()

for _ in range(C):
    color = input().strip()

    now = colors
    for item in color:
        if not now.get(item):
            now[item] = dict()
        now = now[item]
    now[0] = 1

nicknames = set([input().strip() for _ in range(N)])

Q = int(input().strip())

for _ in range(Q):
    name = input().strip()
    length = len(name)

    result = 'No'

    now = colors
    for i in range(length):
        if now.get(0) and name[i:] in nicknames:
            result = 'Yes'
            break
        if not now.get(name[i]):
            break
        now = now[name[i]]
    
    print(result)