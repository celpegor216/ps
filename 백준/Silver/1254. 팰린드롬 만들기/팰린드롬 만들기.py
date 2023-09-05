S = input()
length = len(S)

result = 0
for i in range(length):
    flag = 1

    start, end = i, length - 1
    while start <= end:
        if S[start] != S[end]:
            flag = 0
            break
        start += 1
        end -= 1

    if flag:
        result = length + i
        break

print(result)