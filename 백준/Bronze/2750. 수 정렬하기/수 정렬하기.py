# 퀵 정렬 설명 참고

N = int(input())
lst = [int(input()) for _ in range(N)]

def quick_sort(s, e):
    if s >= e:
        return

    pivot = lst[s]
    left = s + 1
    right = e

    while left < right:
        while left <= e and lst[left] < pivot:
            left += 1

        while right > s and lst[right] >= pivot:
            right -= 1

        if left > right:
            left = right
            break

        if left != right:
            lst[left], lst[right] = lst[right], lst[left]

    if lst[left] > pivot:
        lst[left - 1], lst[s] = lst[s], lst[left - 1]
        quick_sort(s, left - 2)
        quick_sort(left, e)
    else:
        lst[left], lst[s] = lst[s], lst[left]
        quick_sort(s, left - 1)
        quick_sort(left + 1, e)

quick_sort(0, N - 1)

print(*lst)