A, B = map(int, input().split())
lst_A = sorted(map(int, input().split()))
lst_B = sorted(map(int, input().split()))

result = []

b = 0
for a in range(A):
    while b < B and lst_B[b] < lst_A[a]:
        b += 1
    
    if b == B:
        result += lst_A[a:]
        break
    
    if lst_A[a] != lst_B[b]:
        result.append(lst_A[a])

print(len(result))

if result:
    print(*result)