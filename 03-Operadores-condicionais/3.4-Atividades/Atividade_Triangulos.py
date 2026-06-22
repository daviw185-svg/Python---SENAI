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