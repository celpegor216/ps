N = int(input())
lst = [int(input()) for _ in range(N)]

lst.sort()

result = 4

start = 0
for end in range(1, N):
    diff = lst[end] - lst[start]

    if diff <= 4:
        result = min(result, 5 - (end - start + 1))
    else:
        while start <= end and lst[end] - lst[start] >= 5:
            start += 1

    if not result:
        break

print(result)