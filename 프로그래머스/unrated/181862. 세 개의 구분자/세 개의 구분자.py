def solution(myStr):
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    
    answer = myStr.split()
    
    if not answer:
        answer = ['EMPTY']
    
    return answer