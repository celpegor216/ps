N = int(input())
lst = list(map(int, input().split()))

result = -1
for i in range(N - 1, 0, -1):
    if lst[i] > lst[i - 1]:
        if i > 0:
            temp = lst[:i - 1] + [min([x for x in lst[i - 1:] if x > lst[i - 1]])]
        else:
            temp = [lst[0] + 1]

        result = temp + [x for x in range(1, N + 1) if x not in temp]
        break

if result != -1:
    print(*result)
else:
    print(result)