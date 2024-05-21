import sys
input = sys.stdin.readline

def search(now):
    global result

    if not children[now]:
        if not marbles[now]:
            return 0, [1]
        else:
            return marbles[now] - 1, []

    left = 0
    need = []
    for child in children[now]:
        l, n = search(child)
        left += l
        need += n
    need.sort()

    cnt = marbles[now] + left
    result += left
    
    while cnt > 1 and need:
        cnt -= 1
        result += need.pop()
    
    for i in range(len(need)):
        need[i] += 1
    
    if not cnt:
        need.append(1)
        return cnt, need
    else:
        return cnt - 1, need

while 1:
    N = int(input())

    if not N:
        break

    parent = [0] * (N + 1)
    children = [[] for _ in range(N + 1)]
    marbles = [0] * (N + 1)

    for _ in range(N):
        tmp = list(map(int, input().strip().split()))
        marbles[tmp[0]] = tmp[1]
        children[tmp[0]] = tmp[3:]
        for child in tmp[3:]:
            parent[child] = tmp[0]

    result = 0

    root = 0
    for i in range(1, N + 1):
        if not parent[i]:
            root = i
            break

    cnt, need = search(root)
    result += sum(need)
    print(result)