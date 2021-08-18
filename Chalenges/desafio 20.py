from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
sorteio = [a1, a2, a3, a4]
shuffle(sorteio)
print('A ordem sorteada foi: ')
print(sorteio)


