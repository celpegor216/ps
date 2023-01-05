# f(1) = 1 = 1
# f(2) = 1+1, 2 = 2
# f(3) = 1+2, 1+1+1, 2+1, 3 = 4
# f(4) = 1+2+1, 1+1+1+1, 2+1+1, 3+1, 1+1+2, 2+2, 1+3 = 7
# ...
# f(k) = f(k-3) + f(k-2) + f(k-1) (단, k > 3)

T = int(input())

memo = [0, 1, 2, 4]

for k in range(4, 11):
    memo.append(memo[k-3] + memo[k-2] + memo[k-1])

for t in range(T):
    n = int(input())

    print(memo[n])