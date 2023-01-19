def solution(progresses, speeds):
    answer = []
    
    while progresses:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        
        if progresses[0] >= 100:
            cnt = 0
            
            idx = 0
            while progresses and idx < len(progresses):
                if progresses[idx] >= 100:
                    progresses.pop(idx)
                    speeds.pop(idx)
                    cnt += 1
                else:
                    break
            
            answer.append(cnt)
    
    return answer