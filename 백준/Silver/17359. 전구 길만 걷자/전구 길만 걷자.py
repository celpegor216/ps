N = int(input())
lst = []
fixed_result = 0
for _ in range(N):
    S = input()

    starts_with = 1 if S[0] == '1' else 0
    ends_with = 1 if S[-1] == '1' else 0
    lst.append((starts_with, ends_with))

    cnt = 0
    now = S[0]
    for i in range(1, len(S)):
        if now != S[i]:
            cnt += 1
            now = S[i]
    fixed_result += cnt


used = [0] * N

result = 21e8
def dfs(level, order):
    global result

    if level == N:
        total = 0
        now = lst[order[0]][1]
        for i in range(1, N):
            if lst[order[i]][0] != now:
                total += 1
            now = lst[order[i]][1]
        result = min(result, fixed_result + total)
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, order + [i])
            used[i] = 0

dfs(0, [])

print(result)