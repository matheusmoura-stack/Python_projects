oi = dict()
oi['nome'] = str(input('Nome: '))
oi['media'] = float(input(f"média de {oi['nome']}: "))
print(f'Nome é igual a {oi["nome"]}')
print(f'Média é igual a {oi["media"]}')
if oi['media'] <= 7:
    print(f'A situação de {oi["nome"]} é: \033[31mREPROVADO\033[m')
else:
    print(f'A situação de {oi["nome"]} é: \033[33mAPROVADO\033[m')
