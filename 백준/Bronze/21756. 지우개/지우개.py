N = int(input())

lst = [x for x in range(1, N + 1)]

while len(lst) > 1:
    tmp = []
    
    for n in range(1, len(lst), 2):
        tmp.append(lst[n])
    
    lst = tmp[:]

print(lst[0])