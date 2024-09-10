U, N = map(int, input().split())
dic = dict()
for _ in range(N):
    name, cost = input().split()
    cost = int(cost)

    dic[cost] = dic.get(cost, []) + [name]

result = sorted(dic.items(), key=lambda x: (len(x[1]), x[0]))[0]
print(result[1][0], result[0])