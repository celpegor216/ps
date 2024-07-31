# 완전 탐색하면 시간초과인데 완전 탐색을 하지 않고 최고 득점을 찾는 방법을 모르겠음
# 해답: https://edder773.tistory.com/60
# 완전 탐색은 맞고 득점을 구하는 부분에서 시간을 줄여야 했음

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

used = [0] * 9
used[0] = 4
result = 0
pluses = {1: 1, 2: 11, 3: 111, 4: 1111}

def dfs(level):
    global result

    if level == 9:
        order = [used.index(x) for x in range(1, 10)]
        total = 0
        now = 0

        for n in range(N):
            out = 0
            b1 = b2 = b3 = 0

            while out < 3:
                if lst[n][order[now]] == 0:
                    out += 1
                elif lst[n][order[now]] == 1:
                    total += b3
                    b1, b2, b3 = 1, b1, b2
                elif lst[n][order[now]] == 2:
                    total += b3 + b2
                    b1, b2, b3 = 0, 1, b1
                elif lst[n][order[now]] == 3:
                    total += b3 + b2 + b1
                    b1, b2, b3 = 0, 0, 1
                elif lst[n][order[now]] == 4:
                    total += b3 + b2 + b1 + 1
                    b1 = b2 = b3 = 0
                now += 1
                if now == 9:
                    now = 0

            result = max(result, total)
        return

    for i in range(1, 10):
        if i not in used:
            used[level] = i
            dfs(level + 1)
            used[level] = 0

dfs(1)

print(result)