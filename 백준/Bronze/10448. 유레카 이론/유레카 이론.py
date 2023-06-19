T = int(input())

lst = [0, 1]

for i in range(2, 45):
    lst.append(lst[i - 1] + i)

nums = set()

def dfs(level, total):
    if level == 3:
        nums.add(total)
        return

    for i in range(1, 45):
        dfs(level + 1, total + lst[i])

dfs(0, 0)

for t in range(T):
    K = int(input())

    if K in nums:
        print(1)
    else:
        print(0)