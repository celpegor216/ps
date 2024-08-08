N = int(input())
lst = list(map(int, input().split()))    # 숫자 순서는 그대로
calcs = list(map(int, input().split()))    # +, -, *, /

result_max = -21e8
result_min = 21e8

def calculate(tmp):
    res = lst[0]

    for n in range(N - 1):
        if tmp[n] == 0:
            res += lst[n + 1]
        elif tmp[n] == 1:
            res -= lst[n + 1]
        elif tmp[n] == 2:
            res *= lst[n + 1]
        elif tmp[n] == 3:
            # 음수를 양수로 나누는 경우
            if res < 0 and lst[n + 1] > 0:
                res = -(-res // lst[n + 1])
            else:
                res //= lst[n + 1]

    return res

def dfs(level, now):
    global result_min, result_max

    if level == N - 1:
        result = calculate(now)
        result_min = min(result_min, result)
        result_max = max(result_max, result)
        return

    for n in range(4):
        if calcs[n]:
            calcs[n] -= 1
            dfs(level + 1, now + [n])
            calcs[n] += 1

dfs(0, [])

print(result_max)
print(result_min)