# 해답: https://velog.io/@imnotmoon/Python-%EB%B0%B1%EC%A4%80-17136.-%EC%83%89%EC%A2%85%EC%9D%B4-%EB%B6%99%EC%9D%B4%EA%B8%B0

lst = [list(map(int, input().split())) for _ in range(10)]
left = [5] * 5
result = 21e8

def dfs(y, x, cnt):
    global left, result

    if y >= 10:
        result = min(result, cnt)
        return
    
    if x >= 10:
        dfs(y + 1, 0, cnt)
        return
    
    if lst[y][x]:
        for k in range(5):
            if left[k] == 0: continue
            if y + k >= 10 or x + k >= 10: continue

            flag = 0
            for i in range(k + 1):
                if flag: break

                for j in range(k + 1):
                    if not lst[y + i][x + j]:
                        flag = 1
                        break
            
            if flag: break

            for i in range(k + 1):
                for j in range(k + 1):
                    lst[y + i][x + j] = 0
            left[k] -= 1

            dfs(y, x + k + 1, cnt + 1)

            for i in range(k + 1):
                for j in range(k + 1):
                    lst[y + i][x + j] = 1
            left[k] += 1
    else:
        dfs(y, x + 1, cnt)

dfs(0, 0, 0)
print(-1 if result == 21e8 else result)