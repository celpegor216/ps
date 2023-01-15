def solution(sizes):
    max_w, max_h = 0, 0
    
    # 가로가 세로보다 더 길게 변경
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
    
        max_w = max(max_w, size[0])    
        max_h = max(max_h, size[1])    
    
    return max_w * max_h