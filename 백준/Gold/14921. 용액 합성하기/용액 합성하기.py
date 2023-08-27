N = int(input())
lst = sorted(map(int, input().split()))

result = 21e8
start, end = 0, N - 1

while start < end:
    tmp = lst[start] + lst[end]

    if abs(tmp) < abs(result):
        result = tmp

    if tmp > 0:
        end -= 1
    else:
        start += 1

print(result)