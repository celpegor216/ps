def solution(new_id):
    answer = ''
    
    check = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    
    if 3 <= len(new_id) <= 15:
        flag = 0
        
        for s in new_id:
            if s not in check:
                flag = 1
                break
        
        if not flag:
            if new_id[0] != '.' and new_id[-1] != '.' and '..' not in new_id:
                return new_id
    
    new_id = new_id.lower()
    
    for s in new_id:
        if s in check:
            if s == '.':
                if len(answer) > 0 and answer[-1] != '.':
                    answer += s
            else:
                answer += s
    
    if answer:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    new_id = answer
    
    if not new_id:
        new_id = 'a'
    
    if len(new_id) <= 2:
        return new_id + new_id[-1] * (3 - len(new_id))
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
        
    return new_id