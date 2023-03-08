def solution(arrayA, arrayB):
    answer = 0
    length = len(arrayA)
    
    # 각 배열의 공약수 구하기
    def find(num):
        half = int(num ** 0.5)
        
        result = set()
        
        for i in range(1, half + 1):
            if not num % i:
                result.add(i)
                result.add(num // i)
        
        return result
    
    arrayA.sort(reverse=True)
    arrayB.sort(reverse=True)
    arrayA_lst = find(arrayA[0])
    arrayB_lst = find(arrayB[0])
    deleteA = set()
    deleteB = set()
    
    for i in range(1, length):
        for item in arrayA_lst:
            if arrayA[i] % item:
                deleteA.add(item)
        
        for item in arrayB_lst:
            if arrayB[i] % item:
                deleteB.add(item)
    
    arrayA_lst -= deleteA
    arrayB_lst -= deleteB
    
    for item in arrayA_lst:
        flag = 0
        
        for num in arrayB:
            if not num % item:
                flag = 1
                break
        
        if not flag:
            answer = max(item, answer)
    
    for item in arrayB_lst:
        flag = 0
        
        for num in arrayA:
            if not num % item:
                flag = 1
                break
        
        if not flag:
            answer = max(item, answer)
    
    return answer