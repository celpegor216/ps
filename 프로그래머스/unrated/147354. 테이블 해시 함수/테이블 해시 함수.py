def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    data = [[]] + data
    
    bits = []
    
    for i in range(row_begin, row_end + 1):
        bits.append(sum([x % i for x in data[i]]))
    
    answer = bits[0]
    
    for i in range(1, len(bits)):
        answer = answer ^ bits[i]
    
    return answer