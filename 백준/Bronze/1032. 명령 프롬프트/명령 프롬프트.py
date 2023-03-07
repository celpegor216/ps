N = int(input())
lst = [input() for _ in range(N)]
length = len(lst[0])

result = list(lst[0])

for i in range(length):
    for n in range(1, N):
        if lst[n][i] != result[i]:
            result[i] = '?'
            break

print(''.join(result))