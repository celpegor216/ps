def solution(n):
    return sum(range(1, n + 1, 2)) if n % 2 else sum([x ** 2 for x in range(2, n + 1, 2)]) 