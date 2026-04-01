h=int(input("quantos habitantes a sua cidade tem: "))
i=1
medsala=0
medfil=0
contsa=0
contfi=0
maiorsala=0
poor=0
while i<=h:
    x=float(input("Digite seu salário: "))
    y=int(input("Digite a quantidade de filhos: "))
    medsala+=x
    medfil+=y
    contsa+=1
    contfi+=1
    if x>maiorsala:
        maiorsala=x
    if x<100:
        poor+=1
    i+=1
mediasala=medsala/contsa
mediafil=medfil/contfi
percentual=poor/h*100
print("média salarial: ",mediasala)
print("média de filhos: ",mediafil)
print("maior salário: ",maiorsala)
print("percentual de pessoas com salário até R$100,00: ",percentual,"%")