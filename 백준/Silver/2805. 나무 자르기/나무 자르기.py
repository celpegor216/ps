N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst) - 1    # 가져가려고 하는 나무 길이 M의 최소가 1이므로
result = 0

while start <= end:
    middle = (start + end) // 2    # 절단기에 설정할 높이

    total = 0    # middle 높이에서 잘랐을 때 얻을 수 있는 나무의 길이 총합
    for item in lst:
        total += item - middle if item > middle else 0

    if total >= M:    # 필요한 나무 길이보다 더 많이 얻을 수 있는 경우
        result = max(result, middle)
        start = middle + 1
    else:
        end = middle - 1

print(result)