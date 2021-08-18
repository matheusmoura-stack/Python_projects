velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado no valor de {}R$ pelo excesso de valocidade.'.format((velocidade-80) *7))
else:
    print('Você não foi multado, continue seu percurso')
print('Tenha um bom dia! dirija com segurança')
