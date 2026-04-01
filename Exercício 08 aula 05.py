n=int(input("Digite um número inteiro: "))
a=2
b=3
soma=0
i=1
while i<=n:
    soma = soma+a
    soma2=a+b
    a=b
    b=soma2
    i+=1
print(soma)