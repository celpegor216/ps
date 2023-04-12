def solution(n, stations, w):
    answer = 0
    length = len(stations)
    r = 1 + w * 2
    
    for i in range(length + 1):
        if i == 0:
            if stations[i] - w - 1 != 0:
                start, end = 1, stations[i] - w - 1
            else:
                continue
        elif 0 < i < length:
            start = stations[i - 1] + w + 1
            end = stations[i] - w - 1
        else:
            if stations[i - 1] != n:
                start = stations[i - 1] + w + 1
                end = n
            else:
                break
        
        answer += (end - start + 1) // r
        if (end - start + 1) % r:
            answer += 1

    return answer