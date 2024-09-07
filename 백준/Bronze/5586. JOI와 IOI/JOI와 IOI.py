S = input()

targets = ['JOI', 'IOI']
results = [0] * 2

for i in range(2):
    for j in range(len(S) - 2):
        if S[j:j + 3] == targets[i]:
            results[i] += 1

for item in results:
    print(item)