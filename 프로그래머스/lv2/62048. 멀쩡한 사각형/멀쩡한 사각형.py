# 해답: https://dev-note-97.tistory.com/49

def solution(w, h):
    answer = w * h
    
    small = min(w, h)
    
    for i in range(1, small + 1):
        if not w % i and not h % i:
            LCM = i
    
    return answer - (w // LCM + h // LCM - 1) * LCM