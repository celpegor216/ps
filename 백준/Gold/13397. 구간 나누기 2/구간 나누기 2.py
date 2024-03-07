# 시간초과
# 접근 자체가 틀렸음(정답은 이분탐색)
# 해답: https://lkitty0302.tistory.com/10

N, M = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, max(lst)
result = end

def check(middle):
    minv = maxv = lst[0]
    m = 1

    for item in lst:
        maxv = max(maxv, item)
        minv = min(minv, item)

        if maxv - minv > middle:
            m += 1
            minv = maxv = item
    
    return M >= m    # M개 이하의 구간으로 나누므로

while start <= end:
    middle = (start + end) // 2

    if check(middle):
        result = min(result, middle)
        end = middle - 1
    else:
        start = middle + 1

print(result)