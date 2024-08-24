# 단, 앞의 과목을 응시하지 않으면 뒤의 과목을 응시할 수 없는 구조이며
# 응시하지 않은 과목의 표준점수는 0점이라고 가정

T = int(input())
lst = list(map(int, input().split())) + [0] * (5 - T)    # 국 수 영 탐 외

result = 0

if lst[0] > lst[2]:
    result += (lst[0] - lst[2]) * 508
else:
    result += (lst[2] - lst[0]) * 108

if lst[1] > lst[3]:
    result += (lst[1] - lst[3]) * 212
else:
    result += (lst[3] - lst[1]) * 305

result += lst[-1] * 707

print(result * 4763)