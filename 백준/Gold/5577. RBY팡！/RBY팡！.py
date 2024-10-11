N = int(input())
lst = [int(input()) for _ in range(N)]

result = N

def check(i):
    global result

    left = i - 1
    right = i + 1

    color = lst[i]
    cnt = 1
    total = 0

    while 1:
        while left >= 0 and lst[left] == color:
            cnt += 1
            left -= 1

        while right < N and lst[right] == color:
            cnt += 1
            right += 1

        if cnt < 4:
            break

        total += cnt
        cnt = 0

        if left >= 0:
            color = lst[left]
        elif right < N:
            color = lst[right]
        else:
            break

    result = min(result, N - total)


for i in range(N):
    now = lst[i]

    # 왼쪽과 다른 경우 왼쪽과 같은 색으로 바꿔보기
    if i > 0 and lst[i - 1] != lst[i]:
        lst[i] = lst[i - 1]
        check(i)
        lst[i] = now

    # 오른쪽과 다른 경우 오른쪽과 같은 색으로 바꿔보기
    if i < N - 1 and lst[i + 1] != lst[i]:
        lst[i] = lst[i + 1]
        check(i)
        lst[i] = now


print(result)