N = int(input())
S = input()
length = len(S)

dic = dict()
result = 0

start, end = 0, 0

while end < length:
    if dic.get(S[end]):
        dic[S[end]] += 1
    else:
        while len(dic) == N:
            dic[S[start]] -= 1
            if dic[S[start]] == 0:
                dic.pop(S[start])
            start += 1
        dic[S[end]] = 1
    result = max(result, end - start + 1)
    end += 1

print(result)