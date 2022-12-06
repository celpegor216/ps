# 입력값 - 롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열 topping
# 출력값 - 롤케이크를 공평하게 자르는 방법의 수, 방법이 없는 경우 0

def solution(topping):
    answer = 0
    
    max_num = max(topping) + 1
    
    bucket_left = [0] * max_num
    bucket_right = [0] * max_num

    bucket_left_num = 0
    bucket_right_num = 0
    
    for item in topping:
        if bucket_right[item] == 0:
            bucket_right_num += 1
        bucket_right[item] += 1
    
    for i in range(len(topping)):
        if bucket_left[topping[i]] == 0:
            bucket_left_num += 1
        bucket_left[topping[i]] += 1
        
        bucket_right[topping[i]] -= 1
        if bucket_right[topping[i]] == 0:
            bucket_right_num -= 1
            
        if bucket_left_num == bucket_right_num:
            answer += 1
    
    return answer