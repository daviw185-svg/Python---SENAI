# dados do usuário, realiza conversões e cálculos simples
print ("Bem-Vindo ao curso de Python!!\n Para aprendermos juntos, preciso que você preencha as informações abaixo:")
nome = (input("Digite seu nome completo: "))
idade = (input("Digite a sua idade: "))
nivel = (input("Em qual nível de conhecimento você se considera? (Iniciante, Intermediário, Avançado, Sênior): "))

idade_atual = int(idade)
print (f'Muito bem, {nome}!')
print (f'Daqui 1 ano, quando você estiver com {idade_atual + 1} anos, você irá adquirir conhecimento de Python nível 2!')