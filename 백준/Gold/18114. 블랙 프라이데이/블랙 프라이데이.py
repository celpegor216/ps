# 해답: https://velog.io/@ktaewon98/BaekjoonPython-18114%EB%B2%88-%EB%B8%94%EB%9E%99%ED%94%84%EB%9D%BC%EC%9D%B4%EB%8D%B0%EC%9D%B4

N, C = map(int, input().split())
lst = sorted(map(int, input().split()))

def func():
    start, end = 0, N - 1

    while start < end:
        total = lst[start] + lst[end]
        if total == C:
            return 1
        elif total > C:
            end -= 1
        else:
            temp = C - total
            if temp != lst[start] and temp != lst[end] and temp in lst:
                return 1
            start += 1
    return 0

if C in lst:
    print(1)
else:
    print(func())