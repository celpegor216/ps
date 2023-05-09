def solution(n, t, m, timetable):
    answer = 0
    length = len(timetable)
    
    for i in range(length):
        timetable[i] = int(timetable[i][:2]) * 60 + int(timetable[i][3:])
    
    timetable.sort()
    
    start = 540
    idx = 0
    cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if idx < length and timetable[idx] <= start:
                idx += 1
                cnt += 1
            else:
                break
        
        start += t
    
    start -= t
    
    # 마지막 차에 자리가 없다면, 한 명 밀어내고 내가 타야 함
    if cnt >= m:
        answer = timetable[idx - 1] - 1
    # 마지막 차에 자리가 있다면, 내가 갈 수 있는 가장 마지막 시간에 타야 함
    else:
        answer = start
    
    return f'{answer // 60:0>2}:{answer % 60:0>2}'


# 1. 5명 태울 수 있는데 앞에 4명이 다 9시 전에 와서 9시에 타면 됨
# 2. 4명 태울 수 있는데 앞 차는 8시가 타고 뒷 차는 9시 10분에 출발하므로 9시 9분 한 명이랑 내가 9시 9분에 타면 됨
# 3. 4명 태울 수 있는데 넷 다 9시에 왔으므로 나는 8시 59분에 와야 함
# 4. 5명 태울 수 있는데 다섯 다 00시 1분에 왔으므로 나는 00시 00분에 와야 함
# 5. 1명 태울 수 있는데 23:59분에 왔으므로 나는 9시에 타야 함
# 6. 450명 태울 수 있는데 전부 23:59분에 왔으므로 나는 막차에 타야 함