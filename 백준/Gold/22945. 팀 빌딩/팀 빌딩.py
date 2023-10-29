# 힌트: 투 포인터
# 해답:

N = int(input())
lst = list(map(int, input().split()))

left, right = 0, N - 1
result = 0

while left + 1 < right:
    result = max(result, min(lst[left], lst[right]) * (right - left - 1))

    if lst[left] < lst[right]:
        left += 1
    else:
        right -= 1
    
print(result)