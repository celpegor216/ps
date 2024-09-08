N, S = input().split()
N = int(N)
lst = [input().split() for _ in range(N)]

result = 0
answer = ''
for i in range(N - 1, -1, -1):
    if lst[i][0] == S:
        answer = lst[i][1]
    elif answer and lst[i][1] == answer:
        result += 1

print(result)