N, M = map(int, input().split())
dic = dict()

for n in range(N):
    dic[input()] = 1

result = 0
for m in range(M):
    S = input()

    if dic.get(S):
        result += 1

print(result)