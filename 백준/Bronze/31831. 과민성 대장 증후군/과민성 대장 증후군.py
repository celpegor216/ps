N, M = map(int, input().split())
lst = list(map(int, input().split()))

now = 0
result = 0
for item in lst:
    now += item

    if now < 0:
        now = 0

    if now >= M:
        result += 1

print(result)