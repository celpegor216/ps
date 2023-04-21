def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        total = 1
        for item in num_list:
            total *= item
        return total