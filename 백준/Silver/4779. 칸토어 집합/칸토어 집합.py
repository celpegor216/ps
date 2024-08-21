def recursive(n):
    if not memo[n]:
        memo[n] = recursive(n - 1) + ' ' * (3 ** (n - 1)) + recursive(n - 1)
    return memo[n]

while 1:
    try:
        N = int(input())
        memo = [''] * (N + 1)
        memo[0] = '-'
        print(recursive(N))
    except:
        break