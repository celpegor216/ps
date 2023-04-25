# 힌트: 투포인터를 사용해야 함
# 해답: https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL3-%EB%B3%B4%EC%84%9D-%EC%87%BC%ED%95%91-Python
# 효율성 해결 못 함

def solution(gems):
    size = len(set(gems))
    length = len(gems)
    start, end = 0, 0
    dic = {gems[0]: 1}
    answer = []
    
    while 1:
        if len(dic) == size:
            if not answer or end - start < answer[1] - answer[0]:
                answer = [start, end]
            else:
                dic[gems[start]] -= 1
                if not dic[gems[start]]:
                    del dic[gems[start]]
                
                start += 1
        else:
            end += 1
            
            if end == length:
                break
            
            if gems[end] in dic:
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1
                
    return [answer[0] + 1, answer[1] + 1]