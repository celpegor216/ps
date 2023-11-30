def solution(data, ext, val_ext, sort_by):
    idx = ["code", "date", "maximum", "remain"]
    
    answer = sorted([d for d in data if d[idx.index(ext)] < val_ext], key=lambda x: x[idx.index(sort_by)])
    return answer