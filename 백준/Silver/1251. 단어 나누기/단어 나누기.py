S = input()
length = len(S)

result = 'z' * length

for i in range(1, length - 1):
    for j in range(i + 1, length):
        temp = S[:i][::-1] + S[i:j][::-1] + S[j:][::-1]

        result = min(result, temp)

print(result)