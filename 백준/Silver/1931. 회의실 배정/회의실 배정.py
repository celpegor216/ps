N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x: (x[1], x[0]))    # 끝나는 시간 기준으로 정렬

end = -1
result = 0

for n in range(N):
    if lst[n][0] >= end:
        end = lst[n][1]
        result += 1

print(result)