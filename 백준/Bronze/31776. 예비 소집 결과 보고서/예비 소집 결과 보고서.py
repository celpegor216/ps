N = int(input())

result = 0
for _ in range(N):
    tmp = list(map(int, input().split()))

    for i in range(3):
        if tmp[i] == -1:
            if i > 0 and tmp[i + 1:].count(-1) == 2 - i and tmp[:i] == sorted(tmp[:i]):
                result += 1
            break
    else:
        if tmp == sorted(tmp):
            result += 1

print(result)