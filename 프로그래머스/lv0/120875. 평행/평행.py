def solution(dots):
    answer = 0
    
    onetwo, threefour = (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]), (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0])
    onethree, twofour = (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0]), (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0])
    onefour, twothree = (dots[0][1] - dots[3][1]) / (dots[0][0] - dots[3][0]), (dots[1][1] - dots[2][1]) / (dots[1][0] - dots[2][0])
    
    if onetwo == threefour or onethree == twofour or onefour == twothree:
        answer = 1
    
    return answer