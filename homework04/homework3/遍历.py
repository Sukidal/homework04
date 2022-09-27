sum = 1
for i in range(1,101):
    if(i%2==1):
        print(i)
    if(i<50 and i % 2 == 1):
        sum = sum * i
print(sum)
