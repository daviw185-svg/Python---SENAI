print ("Bem-Vindo ao curso de Python!!\n Para aprendermos juntos, preciso que você preencha as informações abaixo:")

nome = (input("Digite seu Nome Completo: "))
idade = (input("Digite sua idade: "))
cursando = (input("Desde que ano você está cursando? ")) 
ling_fav = (input("Qual a sua linguagem favorita? "))
nota_stf = (input("De 0-10, qual nota você dá ao curso? "))

idade_atual = int(idade)
tempo_de_curso = int(cursando)
nota_satisfacao = float(nota_stf)
ANO_ATUAL = 2026

print ('============================================ \n FICHA DO DESENVOLVEDOR \n ============================================')
print (f'Nome: {nome}.\nIdade: {idade_atual}.\nTempo de Curso: {ANO_ATUAL - tempo_de_curso}.\nLinguagem favorita: {ling_fav}.')
print ('============================================')
if (nota_satisfacao <= 4): 
    print (input("Poxa!! O que você acha que podemos melhorar? "))
if (nota_satisfacao == 5): 
    print (input("Bom! O que você acha que podemos melhorar? "))
if (nota_satisfacao > 5): 
    print (input("Legal!! O que você acha que podemos melhorar? "))
print (f'Muito obrigado por sua avaliação, {nome}')