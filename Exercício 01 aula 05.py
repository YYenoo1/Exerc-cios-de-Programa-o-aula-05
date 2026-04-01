i1=0
i2=0
i3=0
i4=0
n=int(input("Digite um número aqui: "))
while n>=0:
    if n<=25:
        print('você está no primeiro intervalo')
        i1+=1
    else:
        if n<=50:
            print('você está no segundo intervalo')
            i2+=1
        else:
            if n<=75:
                print('você está no terceiro intervalo')
                i3+=1
            else:
                print('você está no quarto intervalo')
                i4+=1
    n=int(input("Digite um número aqui: "))
print ('fim do programa')
print('quantidade de números no primeiro intervalo: ',i1)
print('quantidade de números no segundo intervalo: ',i2)
print('quantidade de números no terceiro intervalo: ',i3)
print('quantidade de números no quarto intervalo: ',i4)    