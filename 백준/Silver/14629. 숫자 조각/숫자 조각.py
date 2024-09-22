N = int(input())

# N보다 작으면서 가장 큰 수 만들기
result_value = 0
min_diff = N
used = [0] * 10
def dfs_min(level, now):
    global result_value, min_diff

    if now > N:
        return
    
    diff = N - now
    if diff < min_diff:
        result_value = now
        min_diff = diff
    
    for i in range(10):
        if used[i]:
            continue

        used[i] = 1
        dfs_min(level + 1, now * 10 + i)
        used[i] = 0

dfs_min(0, 0)


if min_diff:
    # N보다 크면서 가장 작은 수 만들기
    used = [0] * 10
    def dfs_max(level, now):
        global result_value, min_diff

        if now >= N:
            diff = now - N
            
            if diff < min_diff:
                result_value = now
                min_diff = diff
            return
        
        for i in range(10):
            if used[i]:
                continue

            used[i] = 1
            dfs_max(level + 1, now * 10 + i)
            used[i] = 0

    dfs_max(0, 0)

print(result_value)