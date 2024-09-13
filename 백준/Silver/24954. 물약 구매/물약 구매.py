N = int(input())
costs = [0] + list(map(int, input().split()))
# discounts[i]: i번 물약을 사면 할인(j번을 d만큼)
discounts = [[] for _ in range(N + 1)]

for n in range(1, N + 1):
    P = int(input())
    for _ in range(P):
        discounts[n].append(list(map(int, input().split())))


result = 21e8
used = [0] * (N + 1)
total_discounts = [0] * (N + 1)
def dfs(level):
    global result

    if level == N:
        total = 0

        for n in range(1, N + 1):
            total += max(1, costs[n] - total_discounts[n])

        result = min(result, total)
        return

    for n in range(1, N + 1):
        if used[n]:
            continue

        used[n] = 1
        for a, b in discounts[n]:
            if not used[a]:
                total_discounts[a] += b

        dfs(level + 1)

        used[n] = 0
        for a, b in discounts[n]:
            if not used[a]:
                total_discounts[a] -= b

dfs(0)

print(result)