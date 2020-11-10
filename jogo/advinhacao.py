import random
print('************************')
print('  Jogo de advinhar')
print('************************')

numeroSorte = random.randrange(0, 102, 2)
print(numeroSorte)
print('Escolha o nivel')
nivel = int(input('1 para Facil, 2 para Medio, 3 para Dificil '))

if(nivel == 1):
    chances = 8

elif nivel == 2:
    chances = 5

elif nivel == 3:
    chances = 3

print("Voce tem {} chances ".format(chances))

acertou = 0
for acertou in range(chances): 

    chute = int(input('Digite um numero ?'))
    print('o numero que voce digitou é {}'.format(chute))

    if(chute == numeroSorte):
        print('parabens voce acertou o numero éra {}\n'.format(numeroSorte))
        break

    
    elif(chute != numeroSorte):
        print('voce errou tente novamente')

        if(chute > numeroSorte):
            print('O numero que voce digitou e maior tento um menor\n')

        elif(chute < numeroSorte):
            print('O numero e menor tente um maior\n')    



print('Voce perdeu tente novamente')
print('fim')




