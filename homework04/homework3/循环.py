l = [1,2,3,4,5]

for i in range(4,-1,-1):
    print(l[i])


i = len(l) - 1
while(i>=0):
    print(l[i])
    i = i - 1


for i in l[::-1]:
    print(i)
    
