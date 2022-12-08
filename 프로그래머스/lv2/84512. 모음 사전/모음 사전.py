cnt = 0
flag = 0
word_global = ''

def dfs(level, path):
    global word_global, cnt, flag
    
    if path == word_global:
        flag = 1
        return
    
    if level < 5:
        for w in 'AEIOU':
            if not flag:
                cnt += 1
                dfs(level + 1, path + w)
    

def solution(word):
    global word_global, cnt
    word_global = word
    
    dfs(0, '')
    
    return cnt