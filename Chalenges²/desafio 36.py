casa = float(input('Qual é o  valor da casa a ser comprada? '))
salario = float(input('Qual é o seu salário atualmente? '))
anos = int(input('Em quantos anos você pretende pagar esta casa? '))
m = anos*12
p = casa/m
if p <= salario*(30/100):
    print('você terá de pagar: R${:.2f} por mês para quitar sua casa em {} anos \n \033[4;40;45mFINANCIAMENTO ACEITO\033[m!!'.format(p, anos))
else:
    print('Você não conseguirá pagar esta casa, pois o valor mensal a ser pago é de: R${:.2f}'.format(p), end='')
    print(' e o mínimo que você pode pagar é: R${} \n\033[4;40;45mFINANCIAMENTO NEGADO\033[m!!'.format(salario*(30/100)))
