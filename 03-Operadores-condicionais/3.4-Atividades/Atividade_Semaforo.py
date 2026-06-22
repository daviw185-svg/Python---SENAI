print ('Vamos a um Simulado de Semáforo')
print ('Preciso que você digite uma das três cores, entre "verde", "amarelo", "vermelho" (use somente letras minúsculas).')
cor = (input('Cor: '))

if cor == "verde": 
    print(f'🟢 -> Pode avançar com atenção.')
elif cor == "amarelo": 
    print(f'🟡 -> Atenção! Prepare-se para parar.')
elif cor == "vermelho": 
    print(f'🔴 -> Pare! Aguarde o sinal verde.')
elif cor != "verde" or "vermelho" or "amarelo":
    print('Cor inválida. Digite verde, amarelo ou vermelho.')