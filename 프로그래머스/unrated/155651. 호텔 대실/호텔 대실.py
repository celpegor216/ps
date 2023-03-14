def solution(book_time):
    answer = 0
    length = len(book_time)
    
    for i in range(length):
        book_time[i][0] = int(book_time[i][0][:2]) * 60 + int(book_time[i][0][-2:])
        book_time[i][1] = int(book_time[i][1][:2]) * 60 + int(book_time[i][1][-2:])
    
    book_time.sort()
    
    while book_time:
        now = book_time.pop(0)
        k = 0
        K = len(book_time)
        
        while k < K:
            if book_time[k][0] >= now[1] + 10:
                now = book_time.pop(k)
                K -= 1
            else:
                k += 1
        
        answer += 1
    
    return answer