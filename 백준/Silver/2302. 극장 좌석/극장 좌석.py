N = int(input())
M = int(input())
lst = [int(input()) for _ in range(M)]

memo = [1, 1, 2]

for i in range(3, 41):
    memo.append(memo[i - 1] + memo[i - 2])

temp = []

if M > 0:
    temp.append(memo[lst[0] - 1])
    for m in range(M - 1):
        temp.append(memo[lst[m + 1] - lst[m] - 1])
    temp.append(memo[N - lst[-1]])
else:
    temp.append(memo[N])

result = 1

for item in temp:
    result *= item

print(result)