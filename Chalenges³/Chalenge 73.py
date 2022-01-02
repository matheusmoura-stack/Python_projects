times = "Atlético-MG", "Palmeiras", "Fortaleza", "Bragantino", "Flamengo", \
        "Corinthians", "Cuiabá", "Fluminense", "Atlético-GO", "Atlético-PR", "Ceará", "Internacional",\
        "Juventude", "Santos", "São-Paulo", "Bahia", "América-MG", "Sport", "Grêmio", "Chapecoense"
print('\033[1;31m_\033[m'*80)
print(f'Lista dos times do Brasileirão 2021: {times} ')
print('\033[1;31m_\033[m'*80)
print(f'Os 5 primeiros são: {times[:5]}')
print('\033[1;31m_\033[m'*80)
print(f'Os últimos 4 times são {times[-4:]}')
print('\033[1;31m_\033[m'*80)
print('Times em ordem alfabética: {} '.format(sorted(times)))
print('\033[1;31m_\033[m'*80)
print(f'O chapecoense está na {times.index("Chapecoense")+1}º posição')
