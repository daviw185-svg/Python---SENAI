sim_nao = (input('Eaí, pronto para a calculaPython?(Sim/Não)'))
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
operacao = (input('Qual operação deseja realizar?(Adição, Subtração, Multiplicação ou Divisão): '))

# Se o usuário digitar corretamente "Adição", "Subtração", "Multiplicação" ou "Divisão" 
# os números que ele escolheu serão somados, ou subtraídos, ou multiplicados ou divididos
if (operacao == "Adição"):
    print(f'{num1} + {num2} = {num1 + num2}')
elif (operacao == "Subtração"):
    print(f'{num1} - {num2} = {num1 - num2}')
elif (operacao == "Multiplicação"):
    print(f'{num1} * {num2} = {num1 * num2}')
elif (operacao == "Divisão"):
 if num1 == 0 or num2 == 0:  
#Aqui é o caso se o user escolha algum dos números,
# seja o "num1" ou(a função do "or") "num2" seja "0", 
# e escolher a operação "Divisão", o resultado será um erro. 
    print('Não foi possível calcular o valor')
 else: 
    print(f'{num1} / {num2} = {num1 / num2}') 
else: 
# Na posição onde o "else" está, se o user digitar na operação qualquer outra coisa que não 
# seja as que estão condicionadas, a operação será considerada inválida
   print("Operação Inválida")


