S = input()
length = len(S)
order = [0] * length
cnt = 1

def find_order(start, end):
    global order, cnt

    if start == end:
        return
    
    if start == end - 1:
        order[start] = cnt
        cnt += 1
        return

    minidx = start

    for i in range(start + 1, end):
        if S[i] < S[minidx]:
            minidx = i
    
    order[minidx] = cnt
    cnt += 1
    
    find_order(minidx + 1, end)
    find_order(start, minidx)

find_order(0, length)

for i in range(1, length + 1):
    for j in range(length):
        if order[j] <= i:
            print(S[j], end='')
    
    print()