# IF simples
idade = int(input('Idade: '))

if idade >= 18: 
    print('Maior de idade')
    print('Acesso Autorizado')

# IF / ELSE 
nome = (input('Aluno: '))
nota = float(input('Nota: '))

if nota >= 7.0:
    print(nome + ': Aprovado')
else:
    print(nome + ': Reprovado')

# if / elif / else
nota = float(input('Nota do Aluno: '))

if nota >= 9.0:
    conceito = 'A'
    situacao = 'Awesome'
elif nota >= 7.0:
    conceito = 'B'
    situacao = 'Aproved'
elif nota >= 5.0:
    conceito = 'C'
    situacao = 'Recuperation'
else:
    conceito = 'D'
    situacao = 'Reproved'

print(f'Conceito: {conceito} | Situação: {situacao}')