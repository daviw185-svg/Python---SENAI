nome = input("Digite seu Nome: ")
nascimento = (input("Digite o ano de seu nascimento: "))

print (type (nome))
print (type (nascimento))

nascimento_int = int(nascimento)

ANO_ATUAL = 2026
idade = ANO_ATUAL - nascimento_int

print (f'Olá, {nome}! Você tem {idade} anos.')

# Por que foi necessário converter o tipo?
# R= Foi necessário converter o tipo para que o dadode nascimento fosse considerado como tipo número inteiro(int).

# O que acontece se a conversão não for feita?
# R= Se a conversão não for feita, o dado de nascimento será considerado como tipo string, e não como número.