x=int(input("Digite um número inteiro: "))
if x<1:
    print("Não é primo")
else:
    cont=0
    for i in range (2, x):
        if x%i==0:
            cont+=1
    if cont==0:
        print("É primo")
    else: 
        print("Não é primo")