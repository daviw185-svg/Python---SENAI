# dados do usuário, realiza conversões e cálculos simples
print ("Bem-Vindo ao curso de Python!!\n Para aprendermos juntos, preciso que você preencha as informações abaixo:")
nome = (input("Digite seu nome completo: "))
nascimento = (input("Digite o ano de seu nascimento: "))
nivel = (input("Em qual nível de conhecimento você se considera? (Iniciante, Intermediário, Avançado): "))

nascimento_int = int(nascimento)
ANO_ATUAL = 2026
idade = ANO_ATUAL - nascimento_int

print (f'Muito bem, {nome}! Você tem {idade} anos agora.')
if (nivel == 'Iniciante'):  
    print (f'Daqui 2 meses, se você fazer 1 módulo por dia, você adquirá o conhecimento de Intermediário!')
if (nivel == 'Intermediário'):  
    print (f'Daqui 6 meses, se você fazer 1 módulo por dia, você adquirá o conhecimento de Avançado!')
if (nivel == 'Avançado'):  
    print (f'Daqui 1 ano, se você fazer 1 módulo por dia, você adquirá o conhecimento de Sênior!')

