def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        a = bin(arr1[i])[2:]
        b = bin(arr2[i])[2:]
        temp = ''

        if len(a) < n:
            a = '0' * (n - len(a)) + a
        if len(b) < n:
            b = '0' * (n - len(b)) + b
        
        print(a, b)
        
        for s in range(n):
            if a[s] == '1' or b[s] == '1':
                temp += '#'
            else:
                temp += ' '
        
        answer.append(temp)
    
    return answer