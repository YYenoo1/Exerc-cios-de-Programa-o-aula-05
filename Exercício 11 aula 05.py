contador=1
a=0
b=0
c=0
medalt=0
while contador<=25:
    idade=int(input("Digite a sua idade: "))
    altura=float(input("Digite a sua altura: "))
    peso=float(input("Digite o seu peso: "))
    if idade>50:
        a+=1
    if 10<=idade<=20:
        b+=1
        medalt+=altura
    if peso<50:
        c+=1
    contador+=1
    perc=(c/25)*100
print("A quantidade de pessoas com mais de 50 anos é: ",a)
print("A média de altura das pessoas entre 10 e 20 anos é: ",medalt/b)
print("O percentual de pessoas com peso inferior a 50 kg é: ",perc)