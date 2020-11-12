print('****************')
print('     Forca      ')
print('****************')

palavra_forca = 'metallica'.upper()
palavra_espaco = ['_' for letra in palavra_forca]

acertou = False
enforcou = False
errou = 0

while(not acertou and not enforcou):
    
    chute =input('Escolha uma letra ?')
    chute = chute.strip().upper()

    if(chute in palavra_forca):    
        index = 0
        for letra in palavra_forca:
            if(chute == letra):
                palavra_espaco[index] = letra
            index = index + 1
    else:
        errou = errou + 1
    enforcou = errou == 8   
    acertou = '_' not in palavra_espaco

    print('errou {}'.format(errou))
    print('acertou {} '.format(acertou))
    print(palavra_espaco)   

if(acertou):
    print('Parabens voce ganhou')

elif (enforcou):
    print('fim do jogo, Voce perdeu')


