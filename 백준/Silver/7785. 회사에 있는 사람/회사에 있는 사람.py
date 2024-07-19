import sys
input = sys.stdin.readline

N = int(input())
dic = dict()

for _ in range(N):
    name, status = input().split()

    if status == 'enter':
        dic[name] = 1
    else:
        if dic.get(name):
            dic.pop(name)

for name in sorted(dic.keys(), reverse=True):
    print(name)