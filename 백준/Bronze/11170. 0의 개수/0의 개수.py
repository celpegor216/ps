T = int(input())

memo = [0] * (10 ** 6 + 1)

for i in range(1000001):
    memo[i] += str(i).count('0')

for t in range(T):
    N, M = map(int, input().split())

    print(sum(memo[N:M + 1]))