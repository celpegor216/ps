from copy import deepcopy

N = int(input())

max_lst = list(map(int, input().split()))
min_lst = deepcopy(max_lst)

for n in range(1, N):
    a, b, c = map(int, input().split())
    
    max_a = a + max(max_lst[0], max_lst[1])
    min_a = a + min(min_lst[0], min_lst[1])
    
    max_b = b + max(max_lst)
    min_b = b + min(min_lst)
    
    max_c = c + max(max_lst[2], max_lst[1])
    min_c = c + min(min_lst[2], min_lst[1])
    
    max_lst = [max_a, max_b, max_c]
    min_lst = [min_a, min_b, min_c]

print(max(max_lst), min(min_lst))