# 반례 참고
# 해답: https://thought-process-ing.tistory.com/205

# 택배에 가중치가 없으므로 그냥 많이 옮기기만 하면 되는데,
# 이때 가까운 거리의 택배를 먼저 옮기는 것이 좋음


import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
lst = [list(map(int, input().split())) for _ in range(M)]
lst.sort(key=lambda x: x[1])

upper_bound = [C] * (N + 1)    # 각 마을에서의 실을 수 있는 최대치
result = 0

for s, e, c in lst:
    minv = C    # 출발지부터 도착지까지 실을 수 있는 박스의 최대치

    for i in range(s, e):
        minv = min(minv, upper_bound[i])
    
    minv = min(minv, c)    # 최대치와 현재 값 중 더 작은 값만큼만 옮길 수 있음

    for i in range(s, e):    # 출발지부터 도착지 사이의 최대치를 갱신
        upper_bound[i] -= minv

    result += minv

print(result)