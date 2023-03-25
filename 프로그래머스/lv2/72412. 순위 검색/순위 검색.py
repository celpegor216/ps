# 효율성 해결 해답: https://school.programmers.co.kr/questions/27140

def solution(info, query):
    answer = []
    
    dic = {}
    
    for l in ('cpp', 'java', 'python', '-'):
        for p in ('backend', 'frontend', '-'):
            for e in ('junior', 'senior', '-'):
                for s in ('chicken', 'pizza', '-'):
                    dic[f'{l} {p} {e} {s}'] = []
    
    for i in info:
        temp = i.split()
        score = int(temp[-1])
        
        for l in (temp[0], '-'):
            for p in (temp[1], '-'):
                for e in (temp[2], '-'):
                    for s in (temp[3], '-'):
                        dic[f'{l} {p} {e} {s}'].append(score)
                        
    # 시간초과를 해결한 방법
    for key in dic.keys():
        dic[key].sort()
    
    for q in query:
        temp = q.split()
        
        key = f'{temp[0]} {temp[2]} {temp[4]} {temp[6]}'
        score = int(temp[-1])
        
        # 점수
        length = len(dic[key])
        idx = length

        start, end = 0, length - 1

        while start <= end:
            middle = (start + end) // 2

            if score <= dic[key][middle]:
                idx = middle
                end = middle - 1
            else:
                start = middle + 1

        answer.append(length - idx)
        
    return answer