# 해답: https://baby-ohgu.tistory.com/32

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

result = 0

for i in range(N - 2):
    start, end = i + 1, N - 1

    goal = -lst[i]

    max_idx = N

    while start <= end:
        tmp = lst[start] + lst[end]

        if tmp < goal:
            start += 1
        elif tmp == goal:
            if lst[start] == lst[end]:
                result += end - start
            else:
                if max_idx > end:
                    max_idx = end

                    # lst[end]와 같은 값의 개수 구하기
                    while max_idx >= 0 and lst[max_idx - 1] == lst[end]:
                        max_idx -= 1
                    
                result += end - max_idx + 1
            start += 1
        else:
            end -= 1

print(result)