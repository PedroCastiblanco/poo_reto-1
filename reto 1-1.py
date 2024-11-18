a=input()
b=[]
c=0
for i in range(len(a)):
    if(a[i]=="," ):
        b.append(int(a[c:i]))
        c=i+1 
    elif(len(a)-1==i):
        b.append(a[-2])
    
if b[-1]=="+":
    print(b[0]+b[1])
if b[-1]=="-":
    print(b[0]-b[1])
if b[-1]=="*":
    print(b[0]*b[1])
if b[-1]=="/":
    print(b[0]/b[1])





