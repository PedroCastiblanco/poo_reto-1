def Calcu():
    a=input("Ingrese los digitos y el simbolo de la operacion: ")
    b=[]
    c=0
    for i in range(len(a)):
        if(a[i]=="," ):
            b.append(int(a[c:i]))
            c=i+1 
        elif(len(a)-1==i):
            b.append(a[-2])
        
    if b[-1]=="+":
        return print("La suma entre "+str(b[0])+" y "+str(b[1])+" es: "+str(b[0]+b[1]))
    if b[-1]=="-":
        return print("La resta entre "+str(b[0])+" y "+str(b[1])+" es: "+str(b[0]-b[1]))
    if b[-1]=="*":
        return print("La multiplicación entre "+str(b[0])+" y "+str(b[1])+" es: "+str(b[0]*b[1]))
    if b[-1]=="/":
        return print("La division entre "+str(b[0])+" y "+str(b[1])+" es: "+str(b[0]/b[1]))

Calcu()




