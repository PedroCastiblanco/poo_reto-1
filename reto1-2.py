a=input("Escriba la palabra a comprobar: ")
if(len(a)%2==0):
    x:bool=True
    for i in range((len(a)//2)):
        if(a[i]!=a[-(i+1)]):
            x=False
            print(str(a)+" NO es palindromo")
            break
    if x:
        print(str(a)+" es palindromo")
else:
    x:bool=True
    for i in range((len(a)//2)+1):
        if(a[i]!=a[-(i+1)]):
            x=False
            print(str(a)+" NO es palindromo")
            break
    if x:
        print(str(a)+" es palindromo")
