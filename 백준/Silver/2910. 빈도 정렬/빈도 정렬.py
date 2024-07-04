N, C = map(int, input().split())
lst = list(map(int, input().split()))

dic = dict()

for n in range(N):
    if not dic.get(lst[n]):
        dic[lst[n]] = [n, 0]
    dic[lst[n]][1] += 1

for key, value in sorted(dic.items(), key=lambda x: (-x[1][1], x[1][0])):
    print(f'{key} '* value[1], end='')