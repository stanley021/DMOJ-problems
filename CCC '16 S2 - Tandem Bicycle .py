"""Question 1: what is the minimum total speed, out of all possible assignments into pairs?
Question 2: what is the maximum total speed, out of all possible assignments into pairs?"""
Q = int(input())
N = int(input())
dmoj = []
peg = []
output = 0
dmoj_ =  (input().split())
peg_ = (input().split())

for n in range(len(dmoj_)):
    dmoj.append(int(dmoj_[n]))
for n in range(len(peg_)):
    peg.append(int(peg_[n]))
dmoj.sort()
peg.sort()
if Q == 2:
    peg.reverse()

for a,b in zip(dmoj,peg):
    print(sum(max(a,b)))


print(output)



