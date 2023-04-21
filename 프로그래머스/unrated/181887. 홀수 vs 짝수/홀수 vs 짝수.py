def solution(num_list):
    total_odd = 0
    total_even = 0
    
    for i in range(len(num_list)):
        if not i % 2:
            total_odd += num_list[i]
        else:
            total_even += num_list[i]
    
    return max(total_odd, total_even)