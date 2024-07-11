N = int(input())
dic = dict()

for _ in range(N):
    name = input()
    dic[name] = dic.get(name, 0) + 1

print(sorted(dic.items(), key=lambda x: (-x[1], x[0]))[0][0])