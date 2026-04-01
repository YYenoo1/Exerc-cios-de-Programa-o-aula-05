x=int(input("Digite um número inteiro: "))
while x>=0:
    fatorial=1
    contador=1
    while contador<=x:
        fatorial*=contador
        contador+=1
    print(f"O fatorial de {x} é {fatorial}")
    x=int(input("Digite um número inteiro: "))