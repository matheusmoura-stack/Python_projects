salario = float(input('Qual é o seu salário? '))
aumento = salario * (10/100)
aumento2 = salario * (15/100)
if salario > 1250.00:
    print(" Seu aumento foi de: {}R$. \n Seu salário passou a ser {}R$".format(aumento, aumento + salario))
else:
    print(' Seu aumento foi de: {}R$. \n Seu salário passou a ser {}R$'.format(aumento2, aumento2 + salario))



