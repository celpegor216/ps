N = int(input())
lst = list(map(int, input().split()))

temp = []

for i in range(N - 2):
    if not(lst[i] <= lst[i + 1] <= lst[i + 2]) and not(lst[i] >= lst[i + 1] >= lst[i + 2]):
        temp.append(1)
    else:
        temp.append(0)

total = 0
result = 0
for i in range(N - 2):
    if temp[i]:
        total += 1
    else:
        total = 0
    result = max(result, total)

print(result + 2)