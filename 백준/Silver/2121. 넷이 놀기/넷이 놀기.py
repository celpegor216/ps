import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

dic = dict()
plus = 1000000000
maxv = 2000000000

for n in range(N):
    y, x = map(int, input().split())

    dic[(y + plus) * maxv + x] = 1

result = 0
for item in dic.keys():
    if dic.get(item + B) and dic.get(item + A * maxv) and dic.get(item + A * maxv + B):
        result += 1

print(result)