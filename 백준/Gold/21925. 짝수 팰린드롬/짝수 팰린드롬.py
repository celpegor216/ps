N = int(input())
lst = list(map(int, input().split()))

result = 0

start, end = 0, 1

while start < N and end < N:
    if lst[start] == lst[end]:
        s, e = start + 1, end - 1
        flag = 0
        while s < e:
            if lst[s] != lst[e]:
                flag = 1
                break
            s += 1
            e -= 1
        if not flag:
            result += 1
            start = end + 1
            end = start + 1
        else:
            end += 2
    else:
        end += 2

if start != N:
    print(-1)
else:
    print(result)