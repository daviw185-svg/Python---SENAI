numero1 = 10
numero2 = 7

print(numero1 == numero2) # False - igual a
print(numero1 != numero2) # True - diferente de
print(numero1 > numero2) # True - maior que
print(numero1 < numero2) # False - menor que
print(numero1 >= numero2) #True - Maior ou igual
print(numero1 <= numero2) #False - Menor ou igual

# Comparando string

nome = 'David'
print(nome == 'David') # True
print(nome == 'david') # False (case-sensitive)

# operadores Lógicos: and, or, not
idade = 20
tem_habilitacao = True

# and: as DUAS condições precisam ser verdadeiras
pode_dirigir = idade >= 18 and tem_habilitacao
print(pode_dirigir) # True

nota = 6.5
freq = 70

# or: Pelo menos uma precisa ser verdade
precisa_recuperar = nota < 7.0 or freq < 65
print(precisa_recuperar) # True

# not: inverte
print(not True) # False
print(not False) # True
