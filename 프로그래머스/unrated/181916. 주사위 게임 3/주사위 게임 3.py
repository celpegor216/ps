def solution(a, b, c, d):
    answer = 0
    
    bucket = [0] * 7
    
    for i in [a, b, c, d]:
        bucket[i] += 1
    
    if 4 in bucket:
        answer = 1111 * bucket.index(4)
    elif 3 in bucket:
        answer = (10 * bucket.index(3) + bucket.index(1)) ** 2
    elif 2 in bucket:
        if 1 in bucket:
            temp = []

            for i in range(1, 7):
                if bucket[i] == 1:
                    temp.append(i)

            answer = temp[0] * temp[1]
        else:
            temp = []

            for i in range(1, 7):
                if bucket[i] == 2:
                    temp.append(i)

            answer = (temp[0] + temp[1]) * abs(temp[0] - temp[1])
    else:
        answer = min(a, b, c, d)
    
    return answer