def solution(record):
    answer = []
    length = len(record)
    for i in range(length):
        record[i] = record[i].split()
    
    dic = {}
    
    for i in range(length - 1, -1, -1):
        if record[i][1] not in dic.keys() and len(record[i]) > 2:
            dic[record[i][1]] = record[i][2]
    
    for i in range(length):
        if record[i][0] == 'Enter':
            answer.append(f'{dic[record[i][1]]}님이 들어왔습니다.')
        elif record[i][0] == 'Leave':
            answer.append(f'{dic[record[i][1]]}님이 나갔습니다.')
    
    return answer