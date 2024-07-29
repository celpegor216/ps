# 힌트: 밑장 빼기를 나한테만 하는 게 아님...

N = int(input())
lst = list(map(int, input().split()))

result = max(sum(lst[::2]), sum(lst[:N - 2:2]) + lst[-1])
now = sum(lst[:N - 2:2])

for n in range(N // 2 - 1):
    now -= lst[N - 2 * (n + 2)]
    now += lst[N - 1 - (2 * (n + 1))]
    result = max(result, now + lst[-1], now + lst[N - 2 * (n + 2)])

print(result)