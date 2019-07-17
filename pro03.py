# pro03.py
vg=list(map(str,input().split()))
a=len(vg[0])
f=len(vg[1])
s=min(a,c)
if(a>c):
    f=a-c
elif(c>a):
    f=c-a
else:
    f=0
for i in range(s):
    if((c==1 or a==1) and (vg[1][i] in vg[0] )):
        break
    if(vg[0][i]!=vg[1][i]):
        f+=1 
print(f)
