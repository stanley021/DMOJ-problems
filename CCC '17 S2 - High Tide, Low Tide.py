N = int(input())
tides = []
print_list=[]
low_tides = []
high_tides = []
counter = 0

all_tides = (input().split())
for n in range(len(all_tides)):
    tides.append(int(all_tides[n]))
tides.sort()

if N % 2 == 0 :
    low_tides = tides[:(N//2)]
    low_tides.reverse()
    high_tides = tides[(N//2):]
else:
    low_tides = tides[:(N//2)+1]
    low_tides.reverse()
    high_tides = tides[(N//2)+1:]

for n in range(int(N//2)):
    print_list.append((low_tides[n]))
    print_list.append((high_tides[n]))

if N//2 != N/2:
    print_list.append(low_tides[-1])

for n in print_list:
    print(n, end =" ")

print(tides)
print(low_tides)
print(high_tides)

