N = int(input())
dic = dict()

for _ in range(N):
    S = input()
    length = len(S)
    key = [0] * length

    now = 1

    for i in range(length):
        if not key[i]:
            for j in range(i, length):
                if S[i] == S[j]:
                    key[j] = now
            now += 1
    
    res = ''
    for k in key:
        res += chr(ord('a') + k)
    
    dic[res] = dic.get(res, 0) + 1

result = 0
for value in dic.values():
    result += value * (value - 1) // 2

print(result)