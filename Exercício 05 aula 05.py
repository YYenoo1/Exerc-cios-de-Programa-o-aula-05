soma=0
baixo=1
for cima in range (1,100,2):
    soma += cima / baixo
    baixo += 1
print('o valor total de S é de: ',soma)