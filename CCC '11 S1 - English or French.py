n = int(input())
t = 0
s = 0

for y in range(n):
    inp = input()
    for x in range(len(inp)):
        if inp[x] == 't' or inp[x] == 'T':
            t += 1
        if inp[x] == 's' or inp[x] == 'S':
            s += 1

if s > t or t == s:
    print("French")
else:
    print("English")


