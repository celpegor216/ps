def solution(plans):
    # 시작 시간을 기준으로 정렬
    length = len(plans)
    
    for i in range(length):
        plans[i][1] = int(plans[i][1][:2]) * 60 + int(plans[i][1][3:])
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key=lambda x: x[1])
    
    # plans의 앞에서부터 하나씩 뽑아서 검사
    now = plans.pop(0) # 작업 중인 과제
    time = now[1] # 현재 시간
    temp = [] # 중단한 과제
    answer = [] # 결과
    
    while plans:
        # 새로운 과제가 현재 작업 중인 과제가 끝나기 전에 시작한다면
        if time + now[2] > plans[0][1]:
            # 현재 과제를 중단한 과제에 넣고 새로운 과제 시작
            temp.append([now[0], now[1], now[2] - (plans[0][1] - time)])
            now = plans.pop(0)
            time = now[1]
        else:
            # 현재 과제 종료
            time += now[2]
            answer.append(now[0])
            
            # 과제가 끝나자마자 새로운 과제가 시작하거나, 중단한 과제가 없다면 새로운 과제 시작
            if time == plans[0][1] or not temp:
                now = plans.pop(0)
                time = now[1]
            else:
                now = temp.pop()
    
    answer.append(now[0])
    
    for item in temp[::-1]:
        answer.append(item[0])
    
    return answer