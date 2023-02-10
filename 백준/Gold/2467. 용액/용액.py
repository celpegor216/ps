# 해답: https://seongonion.tistory.com/100

N = int(input())
lst = sorted(map(int, input().split()))

left = 0
right = N - 1
result = 21e8
result_left, result_right = left, right

while left < right:
    temp = lst[left] + lst[right]
    
    if abs(temp) < result:
        result = abs(temp)
        result_left = left
        result_right = right
        
        if temp == 0:
            break
            
    if temp < 0: # 작은 쪽 숫자를 더 키워야 함
        left += 1
    else:
        right -= 1
    
print(lst[result_left], lst[result_right])