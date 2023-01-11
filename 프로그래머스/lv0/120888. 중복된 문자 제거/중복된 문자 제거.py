def solution(my_string):
    bucket = [0] * 256
    
    answer = ''
    
    for s in my_string:
        if not bucket[ord(s)]:
            bucket[ord(s)] += 1
            answer += s
    
    return answer