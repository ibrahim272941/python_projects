new=[1,2,3]
new_1=[]
r,l=0,0
for i in new:
    new_1.append(new[l:]+new[:r])
    a=list(reversed(new))
    new_1.append(a[l:]+a[:r])
    l+=1
    r+=1
print(sorted(new_1))