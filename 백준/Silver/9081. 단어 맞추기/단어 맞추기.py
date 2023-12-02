# 해답: https://hbj0209.tistory.com/184

T = int(input())

for t in range(T):
    word = input()
    lst = list(word)
    
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] > lst[i - 1]:
            next_idx = i - 1
            for j in range(len(lst) - 1, -1, -1):
                if lst[i - 1] < lst[j]:
                    next_idx = j
                    break

            lst[i - 1], lst[next_idx] = lst[next_idx], lst[i - 1]

            lst = lst[:i] + sorted(lst[i:])
            break

    print(''.join(lst))