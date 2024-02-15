# 시간 초과
# 해답: https://velog.io/@kcs05008/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-3-%EB%B0%B1%EC%A4%80-12738-python

N = int(input())
lst = list(map(int, input().split()))

# LIS 배열
# 길이만을 구하기 때문에 기존 배열과 순서가 달라도 상관 없음
result = [lst[0]]

for i in range(1, N):
    if result[-1] < lst[i]:
        result.append(lst[i])
    else:
        # lst[i]가 result 배열에서 들어갈 수 있는 위치 찾기
        start, end = 0, len(result) - 1
        idx = -1

        middle = (start + end) // 2

        while start <= end:
            middle = (start + end) // 2

            if result[middle] > lst[i]:
                end = middle - 1
            elif result[middle] < lst[i]:
                start = middle + 1
            else:
                idx = middle
                break

        if idx == -1:
            idx = start
        
        result[idx] = lst[i]

print(len(result))