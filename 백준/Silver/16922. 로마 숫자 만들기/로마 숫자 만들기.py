N = int(input())

num = [1, 5, 10, 50]

result = set()

def find(level, left, total):
    if left == 0:
        result.add(total)
        return

    if level == 3:
        result.add(total + num[level] * left)
        return
    
    for i in range(left + 1):
        find(level + 1, left - i, total + num[level] * i)

find(0, N, 0)

print(len(result))