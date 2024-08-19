A = int(input())
B = int(input())

squares = [x ** 2 for x in range(1, 101)]

left = 101
for i in range(100):
    if A <= squares[i]:
        left = i
        break

right = -1
for i in range(99, -1, -1):
    if B >= squares[i]:
        right = i
        break

if right < left:
    print(-1)
else:
    print(sum(squares[left:right + 1]))
    print(squares[left])