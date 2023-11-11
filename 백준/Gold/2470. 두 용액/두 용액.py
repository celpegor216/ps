# 백준 14921, 2467 이랑 비슷함
# 그냥 투포인터로 풀면 시간초과였던 것 같은데 풀이가 기억나지 않음
# 해답: https://bladejun.tistory.com/97

N = int(input())
lst = sorted(map(int, input().split()))

left, right = 0, N - 1

resultv = 21e8
result = [0, N - 1]

while left < right:
    total = lst[left] + lst[right]

    if resultv > abs(total):
        resultv = abs(total)
        result = [left, right]

    if total < 0:
        left += 1
    else:
        right -= 1

print(lst[result[0]], lst[result[1]])