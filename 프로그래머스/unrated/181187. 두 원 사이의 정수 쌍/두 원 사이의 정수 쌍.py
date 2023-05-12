# 힌트: 모든 점을 for문으로 확인해서 구하는 게 아님
# 해답: https://school.programmers.co.kr/questions/47373

from math import ceil, floor, sqrt

def solution(r1, r2):
    answer = 0
    
    # x축과 y축을 제외한 제1사분면 내부의 점 개수 구하기
    for i in range(1, r2 + 1):
        temp2 = floor(sqrt(r2 ** 2 - i ** 2))
        temp1 = ceil(sqrt(r1 ** 2 - i ** 2)) if r1 > i else 0
        answer += temp2 - temp1 + 1
    
    return answer * 4