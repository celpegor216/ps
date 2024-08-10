N = int(input())
lst = list(map(int, input().split()))

result = [0] * N
first = 0
second = 1
last = N - 1

for n in range(N):
    if lst[n] == 1:
        result[first] = N - n
        while first < N and result[first]:
            first += 1
    elif lst[n] == 2:
        while second < N and not(first < second and not result[second]):
            second += 1
        result[second] = N - n
        second += 1
    else:
        result[last] = N - n
        last -= 1

print(*result)