# 범위가 이분탐색 같은데 식을 어떻게 세워야 하는지 모르겠고 소수점도 되는지 모르겠음
# 해답: https://jinho-study.tistory.com/687

x, y, c = map(float, input().split())

start, end = 0, min(x, y)

result = 0

while end - start > 0.000001:
    middle = (start + end) / 2

    h1 = (x ** 2 - middle ** 2) ** 0.5
    h2 = (y ** 2 - middle ** 2) ** 0.5
    res = h1 * h2 / (h1 + h2)

    if res >= c:
        result = middle
        start = middle
    else:
        end = middle

print(result)