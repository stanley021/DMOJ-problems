A = input()
B = input()
A_list = []
B_list = []
shared = []
anagram = True

if len(A_list)==len(B_list):
    for n in A:
        A_list.append(n)
    for n in B:
        B_list.append(n)

    for n in range(len(A_list)):
        for x in range(len(B_list)):
            if A_list[n] == B_list[x]:
                shared.append(A_list[n])
    for y in shared:
        if y in B_list and y in A_list:
            B_list.remove(y)
            A_list.remove(y)

    for x in B_list:
        if x != "*":
            anagram = False

if anagram == True:
    print("A")
else:
    print("N")

#cccrocks
#socc*rk*