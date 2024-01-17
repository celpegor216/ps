N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

def check(tmp):
    now = tmp[0]
    idx = 1
    used = [0] * N

    while idx < N:
        if tmp[idx] != now:
            if tmp[idx] - now == 1:    # 이동하려는 칸이 1칸 높음
                if idx - L < 0:
                    return 0

                for l in range(1, L + 1):
                    if tmp[idx - l] != now or used[idx - l]:
                        return 0
                    used[idx - l] = 1
                
                now = tmp[idx]
                idx += 1
            elif tmp[idx] - now == -1:    # 이동하려는 칸이 1칸 낮음
                if idx + L - 1 >= N:
                    return 0

                for l in range(L):
                    if tmp[idx + l] != now - 1 or used[idx + l]:
                        return 0
                    used[idx + l] = 1
                
                now = tmp[idx]
                idx += L - 1
            else:
                return 0
        else:
            idx += 1
    
    return 1

result = 0

for n in range(N):
    result += check(lst[n])
    result += check([lst[x][n] for x in range(N)])

print(result)