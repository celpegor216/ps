def solution(before, after):
    bucket_before = [0] * 256
    bucket_after = [0] * 256
    
    for s in before:
        bucket_before[ord(s)] += 1

    for s in after:
        bucket_after[ord(s)] += 1
    
    for i in range(len(bucket_before)):
        if bucket_before[i] != bucket_after[i]:
            return 0
        
    return 1