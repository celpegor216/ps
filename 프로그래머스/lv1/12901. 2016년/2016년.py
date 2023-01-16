def solution(a, b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total = sum(month[:a - 1])
    total += b
    
    total %= 7
    
    return date[total - 1]