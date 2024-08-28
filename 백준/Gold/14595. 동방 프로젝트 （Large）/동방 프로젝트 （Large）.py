N = int(input())
M = int(input())
lst = [list(map(int, input().split())) for _ in range(M)] + [[N, N]]

lst.sort()

result = end = 0

for s, e in lst:
    if end < s:
        result += s - end
        end = e
    else:
        end = max(end, e)

print(result)