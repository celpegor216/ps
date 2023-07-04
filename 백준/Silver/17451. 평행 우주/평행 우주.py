N = int(input())
lst = list(map(int, input().split()))

result = lst[-1]
for n in range(N - 2, -1, -1):
    if result < lst[n]:
        result = lst[n]
    else:
        if result % lst[n]:
            result = lst[n] * ((result // lst[n]) + 1)

print(result)