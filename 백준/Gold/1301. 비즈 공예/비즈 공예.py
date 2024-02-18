# dfs 시간초과, dp 같은데 방법을 모르겠음
# 해답: https://boomrabbit.tistory.com/220

N = int(input())
lst = [0] * 5
for n in range(N):
    lst[n] = int(input())

dp = [[[[[[[-1] * 11
            for _ in range(11)]
              for _ in range(11)]
                for _ in range(11)]
                  for _ in range(11)]
                    for _ in range(6)]
                      for _ in range(6)]

def fun(pprev, prev, a, b, c, d, e):
    if a == 0 and b == 0 and c == 0 and d == 0 and e == 0:
        return 1
    
    result = dp[pprev][prev][a][b][c][d][e]

    if result == -1:
        result = 0
        
        if a > 0 and prev != 1 and pprev != 1:
            result += fun(prev, 1, a - 1, b, c, d, e)
        if b > 0 and prev != 2 and pprev != 2:
            result += fun(prev, 2, a, b - 1, c, d, e)
        if c > 0 and prev != 3 and pprev != 3:
            result += fun(prev, 3, a, b, c - 1, d, e)
        if d > 0 and prev != 4 and pprev != 4:
            result += fun(prev, 4, a, b, c, d - 1, e)
        if e > 0 and prev != 5 and pprev != 5:
            result += fun(prev, 5, a, b, c, d, e - 1)

        dp[pprev][prev][a][b][c][d][e] = result
    
    return result

print(fun(0, 0, *lst))