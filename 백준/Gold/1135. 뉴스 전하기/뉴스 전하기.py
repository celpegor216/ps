# 해답: https://cieske.tistory.com/71

N = int(input())
parents = list(map(int, input().split()))
children = [[] for _ in range(N)]

for n in range(1, N):
    children[parents[n]].append(n)

def dp(now):
    children_times = []

    if children[now]:
        for child in children[now]:
            children_times.append(dp(child))
    else:
        children_times.append(0)
    
    children_times.sort(reverse=True)

    maxv = 0
    for i in range(len(children_times)):
        maxv = max(maxv, children_times[i] + i + 1)
    
    return maxv

print(dp(0) - 1)