N = int(input())

memo = [0] * (N + 1)
memo[0] = 1

def func(n):
    if not memo[n]:
        res = 0

        for i in range(n):
            res += func(i) * func(n - 1 - i)
        
        memo[n] = res

    return memo[n]

print(func(N))