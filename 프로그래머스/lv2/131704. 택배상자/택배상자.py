def solution(order):
    length = len(order)
    num_idx = 1
    ord_idx = 0
    stack = []
    
    while ord_idx < length:
        if num_idx == order[ord_idx]:
            num_idx += 1
            ord_idx += 1
        elif stack and stack[-1] == order[ord_idx]:
            stack.pop()
            ord_idx += 1
        else:
            if num_idx <= length:
                stack.append(num_idx)
                num_idx += 1
            else:
                break
    
    return ord_idx