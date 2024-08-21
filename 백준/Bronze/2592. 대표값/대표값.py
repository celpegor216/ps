N = 10
dic = dict()

total = 0
for _ in range(N):
    num = int(input())

    total += num
    dic[num] = dic.get(num, 0) + 1

print(total // N)

maxv = 0
result = 0
for key in dic.keys():
    if dic[key] > maxv:
        maxv = dic[key]
        result = key

print(result)