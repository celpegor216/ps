N = int(input())

start, end = 0, 2 ** 32
result = end

while start <= end:
    middle = (start + end) // 2

    if middle ** 2 >= N:
        result = middle
        end = middle - 1
    else:
        start = middle + 1

print(result)