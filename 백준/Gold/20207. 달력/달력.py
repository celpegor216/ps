# 반례는 맞는데 계속 틀림
# 해답: https://westmino.tistory.com/102

N = int(input())
lst = [0] * 367

# lst[n]: n일 째의 누적합 == 사각형의 높이
for _ in range(N):
    s, e = map(int, input().split())
    lst[s] += 1
    lst[e + 1] -= 1

result = 0
height = width = 0

for i in range(1, 367):
    lst[i] += lst[i - 1]
    if lst[i] == 0:
        result += height * width
        height = width = 0
    else:
        width += 1
        height = max(height, lst[i])

print(result)