N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()

result = 0

idx = N - 1
while 1:
    if idx >= 2:
        result += lst[idx] + lst[idx - 1]
    else:
        for i in range(idx + 1):
            result += lst[i]
        break

    idx -= 3

print(result)