# 반례 참고, 노래가 다 끝나더라도 벨소리가 울리기 전까지 기다려야함

N, L, D = map(int, input().split())

def find():
    time = 0
    for _ in range(N):
        time += L
        
        for i in range(5):
            if not (time + i) % D:
                return time + i
        time += 5
    
    time -= 5
    
    result = D
    while result < time:
        result += D
    return result

print(find())