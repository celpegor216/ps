def solution(sequence, k):
    answer = []
    
    start_idx = 0
    end_idx = 0
    total = sequence[0]
    
    while end_idx < len(sequence):
        if total == k:
            if not answer or end_idx - start_idx < answer[1] - answer[0] or (end_idx - start_idx == answer[1] - answer[0] and start_idx < answer[0]):
                answer = [start_idx, end_idx]
                
        if total == k or total > k:
            total -= sequence[start_idx]
            start_idx += 1
            
            if start_idx > end_idx and end_idx < len(sequence):
                total += sequence[end_idx]
                end_idx += 1
        else:
            end_idx += 1
            if end_idx < len(sequence):
                total += sequence[end_idx]
            else:
                break
    
    return answer