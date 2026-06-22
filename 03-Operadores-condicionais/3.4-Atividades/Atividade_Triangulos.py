print('Olá, seja muito bem-vindo ao PyTri! Aqui você escolhe os tamanhos dos lados e nós identificamos qual o tipo do triângulo 🔼.')
lado1 = float(input('Digite o tamanho do first lado: '))
lado2 = float(input('Digite o tamanho do second lado: '))
lado3 = float(input('Digite o tamanho do third lado: '))

lado1 < lado2 + lado3 
lado2 < lado1 + lado3
lado3 < lado1 + lado3

if lado1 > lado2 + lado3 :
    print(f'😞 Não foi possível classificar porque o lado "{lado1}" não pode ser maior do que a soma dos outros dois lados')
elif lado1 == lado2 == lado3:
    print(f'Uau 🕵️, você formou um triângulo EQUILÁTERO! Porque todos os lados são iguais.')
elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado2:
    print(f'Uau 🗿🍷, você formou um triângulo ISÓCELES! Porque dois lados são iguais.')
elif lado1 != lado2 != lado3:
    print(f'Uau 😎 , você formou um triângulo ESCALENO! Porque todos os lados tem tamanhos diferentes.')

"""
Olá, seja muito bem-vindo ao PyTri! Aqui você escolhe os tamanhos dos lados e nós identificamos qual o tipo do triângulo 🔼.
Digite o tamanho do first lado: 90.5
Digite o tamanho do second lado: 90.5
Digite o tamanho do third lado: 90.5
Uau 🕵️, você formou um triângulo EQUILÁTERO! Porque todos os lados são iguais.

Olá, seja muito bem-vindo ao PyTri! Aqui você escolhe os tamanhos dos lados e nós identificamos qual o tipo do triângulo 🔼.
Digite o tamanho do first lado: 67.4
Digite o tamanho do second lado: 65
Digite o tamanho do third lado: 67.4
Uau 🗿🍷, você formou um triângulo ISÓCELES! Porque dois lados são iguais.

Olá, seja muito bem-vindo ao PyTri! Aqui você escolhe os tamanhos dos lados e nós identificamos qual o tipo do triângulo 🔼.
Digite o tamanho do first lado: 65
Digite o tamanho do second lado: 60
Digite o tamanho do third lado: 75
Uau 😎 , você formou um triângulo ESCALENO! Porque todos os lados tem tamanhos diferentes.

Olá, seja muito bem-vindo ao PyTri! Aqui você escolhe os tamanhos dos lados e nós identificamos qual o tipo do triângulo 🔼.
Digite o tamanho do first lado: 5
Digite o tamanho do second lado: 3
Digite o tamanho do third lado: 1.6
😞 Não foi possível classificar porque o lado "5.0" não pode ser maior do que a soma dos outros dois lados
"""
