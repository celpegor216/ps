def solution(n):
    if not n % 2 and not n % 3:
        return n // 6
    elif not n % 2:
        return n // 2
    elif not n % 3:
        return n // 3
    else:
        return n
