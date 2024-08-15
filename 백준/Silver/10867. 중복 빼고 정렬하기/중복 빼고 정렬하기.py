N = int(input())
lst = list(set(map(int, input().split())))

def merge_sort(start, end):
    if start == end:
        return [lst[start]]

    middle = (start + end) // 2
    left = merge_sort(start, middle)
    right = merge_sort(middle + 1, end)

    l = r = idx = 0
    tmp = [0] * (end - start + 1)

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            tmp[idx] = left[l]
            idx += 1
            l += 1
        else:
            tmp[idx] = right[r]
            idx += 1
            r += 1
    
    while l < len(left):
        tmp[idx] = left[l]
        idx += 1
        l += 1
    
    while r < len(right):
        tmp[idx] = right[r]
        idx += 1
        r += 1
    
    return tmp

print(*merge_sort(0, len(lst) - 1))