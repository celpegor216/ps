S = input()
length = len(S)

hasL = 0
isVowel = [0] * length
for i in range(length):
    if S[i] in 'AEIOU':
        isVowel[i] = 1
    elif S[i] == '_':
        isVowel[i] = -1
    elif S[i] == 'L':
        hasL = 1

result = 0
def dfs(level, v, c):
    global length, hasL, isVowel, result

    if level == length:
        flag = 0

        cnt = 1
        now = isVowel[0]
        for i in range(1, length):
            if isVowel[i] == now:
                cnt += 1
                if cnt == 3:
                    flag = 1
                    break
            else:
                cnt = 1
                now = isVowel[i]
        
        if not flag:
            if not hasL and c < 1:
                return
            
            vowels = 5 ** v if v > 0 else 1

            if not hasL:
                consonants = 21 ** c - 20 ** c
            else:
                consonants = 21 ** c

            tmp = vowels * consonants if consonants > 0 else vowels
            
            result += tmp
        
        return
    
    if isVowel[level] == -1:
        isVowel[level] = 1
        dfs(level + 1, v + 1, c)
        isVowel[level] = 0
        dfs(level + 1, v, c + 1)
        isVowel[level] = -1
    else:
        dfs(level + 1, v, c)

dfs(0, 0, 0)

print(result)