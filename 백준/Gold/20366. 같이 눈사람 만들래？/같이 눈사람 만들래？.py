N = int(input())
lst = sorted(map(int, input().split()))

result = 21e10

for i in range(N):
    for j in range(i + 1, N):
        now = lst[i] + lst[j]

        start, end = 0, N - 1
        
        while start < end:
            if start in (i, j):
                start += 1
            elif end in (i, j):
                end -= 1
            else:
                tmp = lst[start] + lst[end]
                if abs(now - tmp) >= result:
                    if now > tmp:
                        start += 1
                    else:
                        end -= 1
                else:
                    result = abs(now - tmp)
                    end -= 1

print(result)