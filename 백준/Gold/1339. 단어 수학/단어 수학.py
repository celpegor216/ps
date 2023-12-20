N = int(input())
lst = [input() for _ in range(N)]
dic = dict()

for word in lst:
    length = len(word)
    for i in range(length - 1, -1, -1):
        if not dic.get(word[i]):
            dic[word[i]] = [0] * 8
        dic[word[i]][length - 1 - i] += 1

for k, v in dic.items():
    dic[k] = 0
    for item in v[::-1]:
        dic[k] = dic[k] * 10 + item

result = dict()
num = 9
for k, v in sorted(dic.items(), key=lambda x: -x[1]):
    result[k] = num
    num -= 1

answer = 0
for word in lst:
    total = 0
    for w in word:
        total = total * 10 + result[w]

    answer += total

print(answer)