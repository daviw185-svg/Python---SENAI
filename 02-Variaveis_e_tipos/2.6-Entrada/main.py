# Capturando Texto
nome = input("Digite seu nome: ")
print (f'Olá, {nome}! Seja bem-vindo(a)!')

# Capturando número - COM e SEM conversão
# SEM conversão (errado para cálculos)
# idade = input('idade')
# print(idade + 1) # TypeError

# COM conversão (correto)
# idade = int(input('idade:'))
# print (f'Você tem {idade} anos')
# print (f'Em 12 anos terá {idade+12} anos')


# float
altura = float(input('Digite sua altura(m):'))
print (f'You tem {altura:.2f}m de altura') # :.2f -> formatação para 2 casas decimais

# Constantes, conversão MAIÚSCULAS
PI = 3.14159
NOTA_MINIMA = 7.0
NOME_EMPRESA = 'SHARMY VIDROS'
print(f'Empresa: {NOME_EMPRESA}')
print(f'Nota mínima para aprovação: {NOTA_MINIMA}')

# Validação simples com loop
# Exemplo para idade
while True:
    entrada = input('Write your age: ')
    if entrada.isdigit(): # Verifica se a entrada é um número inteiro
        idade = int(entrada)
        break
    else: 
        print('Erro! Write only numbers for your age.')

        print (f'Your idade is {idade} years old.') 