k=int(input('coloque 10 numeros aqui: '))
maior=k
maior2=k
x=1
while x!=10:
    k=int(input('coloque 10 numeros aqui: '))
    if k>maior:
        maior2=maior
        maior=k
    else:
        if k>maior2:
            maior2=k
    x+=1
print('o maior numero é: ',maior)
print('o segundo maior numero é: ',maior2)