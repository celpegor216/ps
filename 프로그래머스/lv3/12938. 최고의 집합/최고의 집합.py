def solution(n, s):
    if s < n:
        return [-1]
    else:
        answer = []
    
        if not s % n:
            return [s // n] * n
        else:
            left = s % n
            return [s // n] * (n - left) + [(s // n) + 1] * (left)