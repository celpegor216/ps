def solution(arr, delete_list):
    answer = []
    
    for item in arr:
        if item not in delete_list:
            answer.append(item)
    
    return answer