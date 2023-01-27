def solution(fees, records):
    answer = []
    
    dic = {}
    
    for record in records:
        time, num, io = record.split()
        
        if io == 'IN':
            if num in dic.keys():
                dic[num] = [dic[num][0], time, io]
            else:
                dic[num] = [0, time, io]
        else:
            time_in = dic[num][1]
            total = (int(time[:2]) - int(time_in[:2])) * 60 + int(time[3:]) - int(time_in[3:])
            dic[num] = [dic[num][0] + total, time, io]
    
    temp = []
    
    for item in dic.items():
        temp.append(item)
        
    temp.sort(key=lambda x: x[0])
    
    for _, item in temp:
        if item[2] == 'IN':
            item[0] += (23 - int(item[1][:2])) * 60 + 59 - int(item[1][3:])
        
        if item[0] <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1]
            left = item[0] - fees[0]
            if not left % fees[2]:
                fee += (left // fees[2]) * fees[3]
            else:
                fee += (left // fees[2] + 1) * fees[3]
            
            answer.append(fee)
        
    return answer