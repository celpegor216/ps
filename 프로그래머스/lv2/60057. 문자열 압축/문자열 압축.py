def solution(s):
    answer = 21e8
    length = len(s)
    
    # 문자열 자르는 단위를 1부터 길이 절반까지
    for cut in range(1, length + 1):
        temp = ''
        now = s[:cut]
        cnt = 0
        for i in range(1, length // cut + 1):
            if s[cut * i: cut * (i + 1)] == now:
                cnt += 1
            else:
                temp += str(cnt + 1) + now if cnt else now
                now = s[cut * i:cut * (i + 1)]
                cnt = 0
        if length % cut:
            temp += s[-(length % cut):]
        if len(temp) < answer:
            answer = len(temp)
    
    return answer