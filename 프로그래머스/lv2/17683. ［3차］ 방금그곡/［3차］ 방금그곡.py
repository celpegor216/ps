# 힌트: end가 00:00 일때 처리

dic = {'C#': 'H', 'D#': 'I', 'F#': 'J', 'G#': 'K', 'A#': 'L'}

def change(str):
    for key in dic.keys():
        str = str.replace(key, dic[key])
    return str

def solution(m, musicinfos):
    answer = '(None)'
    answer_time = -1
    
    m = change(m)
    
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        melody = change(melody)
        length = len(melody)
        
        if start == end:
            continue
        
        if end == '00:00':
            end = '24:00'
        
        time = int(end[-2:]) - int(start[-2:]) + (int(end[:2]) - int(start[:2])) * 60

        melody = melody * (time // length) + melody[:(time % length)]
            
        if m in melody and time > answer_time:
            answer = title
            answer_time = time
    
    return answer