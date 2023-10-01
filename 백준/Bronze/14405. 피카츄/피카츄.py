S = input()

words = ["pi", "ka", "chu"]

idx = 0
length = len(S)

while 1:
    if length == idx:
        break

    if idx + 2 <= length and S[idx:idx + 2] in words:
        idx += 2
    elif idx + 3 <= length and S[idx:idx + 3] in words:
        idx += 3
    else:
        break

if idx == length:
    print("YES")
else:
    print("NO")