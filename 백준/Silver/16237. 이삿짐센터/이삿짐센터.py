lst = list(map(int, input().split()))

result = lst[-1]

result += lst[3]
lst[0] -= min(lst[0], lst[3])

result += lst[2]
three_two = min(lst[1], lst[2])
lst[2] -= three_two
lst[1] -= three_two
lst[0] -= min(lst[0], lst[2] * 2)

while lst[1]:
    result += 1
    if lst[1] == 1:
        lst[1] = 0
        lst[0] -= min(lst[0], 3)
    else:
        lst[1] -= 2
        lst[0] -= min(lst[0], 1)

result += lst[0] // 5
if lst[0] % 5:
    result += 1

print(result)