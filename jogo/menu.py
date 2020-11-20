import forca
import advinhacao

print('**********************')
print('         Menu         ')
print('**********************')

print('Escolha um jogo')
jogo = int(input(' opção (1) jogo da forca, opcão (2) jogo de advinhar?  '))
print(jogo)

if(jogo == 1):
    forca.jogo()

elif (jogo == 2):
    advinhacao.jogo()    

