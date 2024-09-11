N, D = map(int, input().split())
lst = [0] + sorted(map(int, input().split()))

result = 0
idx = N

for d in range(D):
    while idx and lst[idx] == lst[-1] - d:
        idx -= 1

    result += N - idx

    if lst[-1] - d == 1:
        break

print(result)