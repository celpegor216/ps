N = int(input())
lst = []

for item in map(int, input().split()):
    lst.append([item])

tmp = list(map(int, input().split()))
for n in range(N):
    lst[n].append(tmp[n])

lst.sort(key=lambda x: x[1])

result = 0

for n in range(N):
    result += lst[n][0] + lst[n][1] * n

print(result)