from collections import deque

N, M = map(int, input().split())
# cost_per_weight[i]: i번 주차 공간의 단위 무게당 요금
cost_per_weight = [int(input()) for _ in range(N)]
# weights[i]: i번째 차량의 무게
weights = [0] + [int(input()) for _ in range(M)]

parking_lots = [0] * N
q = deque()

result = 0
for _ in range(M * 2):
    car_idx = int(input())

    if car_idx > 0:
        for i in range(N):
            if not parking_lots[i]:
                parking_lots[i] = -car_idx
                break
        else:
            q.append(-car_idx)
    else:
        for i in range(N):
            if parking_lots[i] == car_idx:
                result += cost_per_weight[i] * weights[-car_idx]
                if q:
                    parking_lots[i] = q.popleft()
                else:
                    parking_lots[i] = 0
    
print(result)