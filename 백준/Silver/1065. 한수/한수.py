N = int(input())

result = 0

for n in range(1, N + 1):
    flag = 1

    tmp = str(n)

    if len(tmp) > 2:
        for i in range(len(tmp) - 2):
            if int(tmp[i]) - int(tmp[i + 1]) != int(tmp[i + 1]) - int(tmp[i + 2]):
                flag = 0
                break

    result += flag

print(result)