_ = int(input())
M = int(input())
lst = list(map(int, input().split()))

MAX = (10 ** 5) * 2
bucket = [0] * (MAX + 1)

if M > MAX:
    print(0)
else:
    for item in lst:
        bucket[item] += 1

    result = 0
    for i in range(1, M // 2 + 1 if M % 2 else M // 2):
        result += min(bucket[i], bucket[M - i])

    if not M % 2:
        result += bucket[M // 2] // 2

    print(result)