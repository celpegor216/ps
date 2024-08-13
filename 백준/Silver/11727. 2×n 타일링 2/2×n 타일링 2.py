n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    memo = [0, 1, 3]

    for i in range(3, n+1):
        memo.append(memo[i-1] + memo[i-2] * 2)

    print(memo[-1] % 10007)