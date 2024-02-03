N = int(input())

dic = dict()

for n in range(N):
    a, b = map(int, input().split())

    if dic.get(b):
        dic[b].append(a)
    else:
        dic[b] = [a]

result = 0

for key in dic.keys():
    dic[key].sort()

    result += dic[key][1] - dic[key][0]

    for i in range(1, len(dic[key]) - 1):
        result += min(dic[key][i + 1] - dic[key][i], dic[key][i] - dic[key][i -1])

    result += dic[key][-1] - dic[key][-2]

print(result)