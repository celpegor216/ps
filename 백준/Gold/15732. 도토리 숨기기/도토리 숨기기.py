# 시간초과 해결 못 하겠음 dp 같긴 한데,,
# 힌트: 이분 탐색
# 해답: https://hwayomingdlog.tistory.com/202

import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(K)]

start = 1
end = N
result = N

while start <= end:
    middle = (start + end) // 2

    total = 0
    for a, b, c in lst:
        if a <= middle <= b:
            total += (middle - a) // c + 1
        elif middle > b:
            total += (b - a) // c + 1
    
    if total >= D:
        result = middle
        end = middle - 1
    else:
        start = middle + 1

print(result)