N = int(input())

lst = []
for _ in range(N):
    name, *birth = input().split()
    lst.append([name, *map(int, birth)])

lst.sort(key=lambda x: (x[-1], x[-2], x[-3]))

print(lst[-1][0])
print(lst[0][0])
