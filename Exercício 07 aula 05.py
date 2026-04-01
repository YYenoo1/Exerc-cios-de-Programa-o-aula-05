x=int(input('coloque um numero inteiro: '))
par=0
impar=0
contpar=0
cont=0
mediap=0
mediag=0
while x!=0:
    if x%2!=0:
        impar+=1
        cont+=1
        mediag+=x
    else:
        par+=1
        contpar+=1
        cont+=1
        mediap+=x
        mediag+=x
    x=int(input('coloque um numero inteiro: '))
medpar=mediap/contpar
medgeral=mediag/cont
print('quantidade de números pares: ',par)
print('quantidade de números ímpares: ',impar)
print('média dos números pares: ',medpar)
print('média geral: ',medgeral)