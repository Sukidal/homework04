s = "abccccda"
if len(s)==0:
    print("0")
s+=' '
ct=1
tem=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        tem+=1
    else:
        ct=max(tem,ct)
        tem=1
print(ct)
