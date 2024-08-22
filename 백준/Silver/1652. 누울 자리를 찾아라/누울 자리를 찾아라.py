N = int(input())
lst = [input() for _ in range(N)]

result_horizontal = 0
# 가로 확인
for i in range(N):
    tmp = lst[i].split('X')
    for item in tmp:
        if len(item) > 1:
            result_horizontal += 1

lst = list(map(list, zip(*lst)))
result_vertical = 0
# 세로 확인
for i in range(N):
    tmp = ''.join(lst[i]).split('X')
    for item in tmp:
        if len(item) > 1:
            result_vertical += 1

print(result_horizontal, result_vertical)