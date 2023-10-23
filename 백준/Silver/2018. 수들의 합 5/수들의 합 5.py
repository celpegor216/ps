N = int(input())

result = 0

start, end = 1, 1
total = 1

while start <= end:
    if total < N:
        end += 1
        total += end
    elif total > N:
        total -= start
        start += 1
    else:
        result += 1
        total -= start
        start += 1
        end += 1
        total += end

print(result)