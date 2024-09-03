N = int(input())
P = int(input())

results = [P]
if N >= 20:
    results.append(int(P * 0.75))
if N >= 15:
    results.append(P - 2000 if P > 2000 else 0)
if N >= 10:
    results.append(int(P * 0.9))
if N >= 5:
    results.append(P - 500 if P > 500 else 0)

print(min(results))