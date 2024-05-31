N = int(input())
lst = list(map(int, input().split()))

stack = []

for item in lst:
    if not stack or stack[-1] < item:
        stack.append(item)
    else:
        start = 0
        end = len(stack) - 1
        idx = end

        while start <= end:
            middle = (start + end) // 2

            if stack[middle] > item:
                idx = min(idx, middle)
                end = middle - 1
            else:
                start = middle + 1

        stack[idx] = item

print(N - len(stack))