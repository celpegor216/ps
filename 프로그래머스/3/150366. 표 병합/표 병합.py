def solution(commands):
    answer = []
    
    groups = [x for x in range(2500)]
    values = [''] * 2500
    
    def find(a):
        if groups[a] != a:
            groups[a] = find(groups[a])
        return groups[a]
    
    def union(a, b):
        group_a, group_b = find(a), find(b)
        
        if group_a != group_b:
            groups[group_b] = group_a
            
            if not values[group_a]:
                values[group_a] = values[group_b]
            values[group_b] = ''
    
    for command in commands:
        c = command.split()
        
        if c[0] == 'UPDATE':
            if len(c) == 4:
                group = find(int(c[1]) * 50 + int(c[2]) - 51)
                values[group] = c[3]
            else:
                for i in range(2500):
                    if values[i] == c[1]:
                        values[i] = c[2]
        elif c[0] == 'MERGE':
            a, b = int(c[1]) * 50 + int(c[2]) - 51, int(c[3]) * 50 + int(c[4]) - 51
            
            if a != b:
                union(a, b)
        elif c[0] == 'UNMERGE':
            pos = int(c[1]) * 50 + int(c[2]) - 51
            group = find(pos)
            
            update = []
            for i in range(2500):
                if find(i) == group:
                    update.append(i)
            
            for idx in update:
                groups[idx] = idx
            
            if values[group] and pos != group:
                values[pos] = values[group]
                values[group] = ''
        else:
            group = find(int(c[1]) * 50 + int(c[2]) - 51)
            
            if values[group]:
                answer.append(values[group])
            else:
                answer.append('EMPTY')
        
    
    return answer