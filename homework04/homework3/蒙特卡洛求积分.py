import random
S = 2
N = 10000000
C = 0
for i in range(N):
    x = random.uniform(0.0,1.0)
    y = random.uniform(0.0,S)
    if y <= (x*x*x + x*x):
        C = C+1
I = C / N * S
print(I)
