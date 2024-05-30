N = int(input())
lst = list(map(int, input().split()))

stack = []

for n in range(N):
    if not stack or stack[-1] < lst[n]:
        stack.append(lst[n])
    else:
        start = 0
        end = len(stack) - 1
        idx = end

        while start <= end:
            middle = (start + end) // 2

            if stack[middle] > lst[n]:
                idx = min(idx, middle)
                end = middle - 1
            else:
                start = middle + 1
        
        stack[idx] = lst[n]
    
print(len(stack))