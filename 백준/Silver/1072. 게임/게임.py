import math

X, Y = map(int, input().split())
Z = math.floor(100 * Y / X)

if Z >= 99:
    print(-1)
else:
    start, end = 0, X * 99
    answer = end

    while start <= end:
        middle = (start + end) // 2

        if math.floor(100 * (Y + middle) / (X + middle)) > Z:
            answer = middle
            end = middle - 1
        else:
            start = middle + 1
    
    print(answer)