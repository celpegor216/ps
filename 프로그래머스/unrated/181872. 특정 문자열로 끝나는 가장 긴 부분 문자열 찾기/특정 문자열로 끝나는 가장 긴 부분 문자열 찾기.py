def solution(myString, pat):
    for i in range(len(myString), -1, -1):
        if myString[i - len(pat):i] == pat:
            return myString[:i]