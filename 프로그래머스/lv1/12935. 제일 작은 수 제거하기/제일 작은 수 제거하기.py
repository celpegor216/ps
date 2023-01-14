def solution(arr):
    arr.pop(arr.index(min(arr)))

    if not arr:
        arr = [-1]
    
    return arr