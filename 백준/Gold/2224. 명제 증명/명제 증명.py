N = int(input())
dic = dict()

for n in range(N):
    a, _, b = input().split()

    if a == b:
        continue

    if not dic.get(a):
        dic[a] = set()
    dic[a].add(b)

result = set()
def dfs(parent, now):

    if not dic.get(now):
        return
    
    for item in dic.get(now):
        if (parent, item) not in result and parent != item:
            result.add((parent, item))
            dfs(parent, item)

for key in sorted(dic.keys()):
    dfs(key, key)

print(len(result))
for item in sorted(result):
    print(f'{item[0]} => {item[1]}')