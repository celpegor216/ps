def recursive(n):
    global cnt_recursive

    if n <= 2:
        cnt_recursive += 1
        return 1
    return recursive(n - 2) + recursive(n - 1)

N = int(input())
cnt_recursive = 0
recursive(N)

print(cnt_recursive, N - 2)