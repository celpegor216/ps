# 해답: https://velog.io/@dasd412/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%AB%EC%9E%90-%EB%B8%94%EB%A1%9D

def solution(begin, end):
    answer = [1] * (end - begin + 1)
    idx = 0
    
    for num in range(begin, end + 1):
        if num == 1:
            answer[idx] = 0
        else:
            if num ** 0.5 > 10000000:
                limit = 10000000
            else:
                limit = int(num ** 0.5)

            for i in range(2, limit + 1):
                if not num % i:
                    answer[idx] = i
                    
                    if num // i <= 10000000:
                        answer[idx] = num // i
                        break
                
        idx += 1
    
    return answer