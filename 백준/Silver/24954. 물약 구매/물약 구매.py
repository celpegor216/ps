N = int(input())
lst = list(map(int, input().split()))

# n번째 물약을 샀을 때, [[a번째 물약을 b만큼 할인], ...]
discounts = [[] for _ in range(N)]
for n in range(N):
    P = int(input())
    for _ in range(P):
        a, b = map(int, input().split())
        discounts[n].append((a - 1, b))

# 지금까지 방문 여부
used = [0] * N
# 지금까지 할인받은 총량
total_discounts = [0] * N
result = N * max(lst) + 1

def dfs(level):
    global result

    if level == N:
        total = 0

        for n in range(N):
            total += max(1, lst[n] - total_discounts[n])
        
        result = min(result, total)
        return
    
    for n in range(N):
        if used[n]:
            continue

        used[n] = 1
        for a, b in discounts[n]:
            # 지금 물약을 사기 이전의 물약은 할인받을 수 없음
            if used[a]:
                continue

            total_discounts[a] += b

        dfs(level + 1)

        used[n] = 0
        for a, b in discounts[n]:
            # 지금 물약을 사기 이전의 물약은 할인받을 수 없음
            if used[a]:
                continue

            total_discounts[a] -= b

dfs(0)

print(result)