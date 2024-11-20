def separar(a:list):
    b=[]
    c=0
    for i in range(len(a)):
        if(a[i]=="," ):
            b.append(int(a[c:i]))
            c=i+1 
        elif(len(a)-1==i):
            b.append(int(a[c:]))
    return b

def Confprim():
    A=input("Ingresar una lista de enteros a verificar: ")
    a=separar(A)
    b=[]
    for i in a:
        c=[(i%(x+1)) for x in range(i)]
        d=c.count(0)
        if d==2 and (i not in b):
            b.append(i)
    return b

#print(separar(input()))
x=Confprim()
x.sort()
print(x)
