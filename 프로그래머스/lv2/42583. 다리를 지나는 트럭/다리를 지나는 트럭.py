from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weigths = truck_weights[::-1]
    
    q = deque([0] * bridge_length)
    total = 0
    
    # 1초가 지날 때마다 맨 앞 하나 빼고
    # 다리 건너는 트럭의 무게 총합이 넘지 않으면 추가
    # 아니면 0 추가
    
    while truck_weights:
        total -= q.popleft()
        
        temp = truck_weights[-1]
        
        if total + temp <= weight:
            q.append(temp)
            total += temp
            truck_weights.pop()
        else:
            q.append(0)
        
        answer += 1
    
    for i in range(bridge_length - 1, -1, -1):
        if q[i]:
            answer += i + 1
            break
    
    return answer