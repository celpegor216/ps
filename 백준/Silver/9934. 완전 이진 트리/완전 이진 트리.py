K = int(input())
lst = [0] + list(map(int, input().split()))
result = [[] for _ in range(K)]

while K > 0:
    K -= 1

    temp = []

    for i in range(len(lst)):
        if i % 2:
            result[K].append(lst[i])
        else:
            temp.append(lst[i])

    lst = temp

for line in result:
    print(*line)