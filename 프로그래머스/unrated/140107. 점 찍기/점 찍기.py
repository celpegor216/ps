# 입력 - 정수 k와 원점과의 거리를 나타내는 정수 d
# 출력 - 점이 총 몇 개 찍히는지

# y ** 2 + x ** 2 <= d ** 2를 만족하는 (y, x)의 개수
# y, x는 0부터 시작, k씩 증가

def solution(k, d):
    answer = 0
    y = 0
    
    while y ** 2 <= d ** 2:
        answer += 1
        answer += int((d ** 2 - y ** 2) ** 0.5) // k
        y += k
    
    return answer