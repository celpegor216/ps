def solution(slice, n):
    return n // slice if not n % slice else n // slice + 1