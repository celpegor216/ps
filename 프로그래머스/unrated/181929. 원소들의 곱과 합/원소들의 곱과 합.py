def solution(num_list):
    mult = 1
    total = 0
    
    for item in num_list:
        mult *= item
        total += item
    
    return 1 if mult < total ** 2 else 0