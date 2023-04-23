def solution(myString, pat):
    changed = ''
    
    for s in myString:
        if s == 'A':
            changed += 'B'
        else:
            changed += 'A'
    
    return 1 if pat in changed else 0