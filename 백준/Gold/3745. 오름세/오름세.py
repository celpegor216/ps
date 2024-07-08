while 1:
    try:
        N = int(input())
        lst = list(map(int, input().split()))

        stack = []

        for n in range(N):
            if not stack or lst[n] > stack[-1]:
                stack.append(lst[n])
            else:
                start = 0
                end = len(stack) - 1
                idx = -1

                while start <= end:
                    middle = (start + end) // 2

                    if stack[middle] < lst[n]:
                        idx = max(idx, middle)
                        start = middle + 1
                    elif stack[middle] == lst[n]:
                        idx = middle - 1
                        break
                    else:
                        end = middle - 1
                
                stack[idx + 1] = lst[n]
        
        print(len(stack))
    except:
        break