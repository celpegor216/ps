N = int(input())
dic = dict()

result = 0
for n in range(N):
    num, flag = map(int, input().split())
    if dic.get(num) in (0, 1) and dic[num] != flag:
        result += 1
    dic[num] = flag

print(result)