# 해답: https://daebaq27.tistory.com/107
# ① n-1개의 원판을 출발 기둥에서 중간 기둥으로 이동 (재귀 호출)
# ② n번째 원판을 출발 기둥에서 도착 기둥으로 이동
# ③ n-1개의 원판을 중간 기둥에서 도착 기둥으로 이동 (재귀 호출)

def solution(n):
    answer = []
    
    def hanoi(start, middle, end, n):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(start, end, middle, n - 1)
            hanoi(start, middle, end, 1)
            hanoi(middle, start, end, n - 1)
            
    hanoi(1, 2, 3, n)
    
    return answer