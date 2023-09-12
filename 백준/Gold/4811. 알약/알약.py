memo = dict()
memo['11'] = 1
memo['2'] = 1

def dfs(now):
    if now in memo.keys():
        return memo[now]
    
    memo[now] = 0

    if '2' in now:
        memo[now] += dfs(now[1:] + '1')

    if '1' in now:
        memo[now] += dfs(now[:-1])

    return memo[now]

dfs('2' * 60)

while 1:
    N = int(input())

    if N == 0:
        break

    print(memo['2' * N])