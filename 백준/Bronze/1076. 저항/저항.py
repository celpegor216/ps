v1 = input()
v2 = input()
mult = input()

lst = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

print((lst.index(v1) * 10 + lst.index(v2)) * 10 ** lst.index(mult))