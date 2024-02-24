import sys
sys.setrecursionlimit(2 ** 30)

N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
target = list(map(int, input().split()))

result = 21e8

def merge(level, cnt, totalr, totalg, totalb):
    global result

    if cnt > 1:
        result = min(result, 
                     abs(target[0] - totalr // cnt) + 
                     abs(target[1] - totalg // cnt) + 
                     abs(target[2] - totalb // cnt))
    
    if level == N:
        return

    if cnt == 7:
        return
    
    merge(level + 1, cnt, totalr, totalg, totalb)
    merge(level + 1, cnt + 1, totalr + colors[level][0], totalg + colors[level][1], totalb + colors[level][2])

merge(0, 0, 0, 0, 0)

print(result)