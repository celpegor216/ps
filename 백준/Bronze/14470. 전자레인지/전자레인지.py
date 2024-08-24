A = int(input())    # 원래 온도
B = int(input())    # 목표 온도
C = int(input())    # 언 고기를 1도 데우는 데 걸리는 시간
D = int(input())    # 언 고기를 해동하는 데 걸리는 시간
E = int(input())    # 얼지 않은 고기를 1도 데우는 데 걸리는 시간

result = 0

if A < 0:
    result += -A * C + D
    A = 0

result += (B - A) * E

print(result)