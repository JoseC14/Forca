import random

print('-----------------------------------------------------')
print('Jogo da Forca')
print('-----------------------------------------------------')

print("Escolha uma das opções abaixo para a palavra")

print("1 - Animais")
print("2 - Comidas")
print("3 - Famosos")
print("4 - Filmes")
print("5 - Jogos")

while True:
    opcao = input("Escolha:")

    if opcao == '1':
        with open('palavras/animais.txt','r') as animais:
            conteudo = animais.read()
            lista_palavras =conteudo.split('\n')
            break
    elif opcao == '2':
        with open('palavras/comidas.txt','r') as comidas:
            conteudo = comidas.read()
            lista_palavras = conteudo.split('\n')
            break
    elif opcao == '3':
        with open('palavras/famosos.txt','r') as famosos:
            conteudo = famosos.read()
            lista_palavras = conteudo.split('\n')
            break
    elif opcao == '4':
        with open('palavras/filmes.txt','r') as filmes:
            conteudo = filmes.read()
            lista_palavras = conteudo.split('\n')
            break
    elif opcao == '5':
        with open('palavras/jogos.txt','r') as jogos:
            conteudo = jogos.read()
            lista_palavras = conteudo.split('\n')
            break
    else:
        print("Opção Inválida! tente novamente")

palavra = random.choice(lista_palavras).lower()
letras = list()

escondida = list()
chances   = 7
for letra in palavra:
    if letra != ' ':
        escondida.append('_')
    else:
        escondida.append(' ')
while True:
    print(escondida)
    print("Letras escolhidas:",letras)
    print("Chances Restantes:", chances)
    if chances == 7:
        print("-------------")
        print("|           |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif chances == 6:
        print("-------------")
        print("|           |")
        print("|           O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif chances == 5:
        print("-------------")
        print("|           |")
        print("|           O")
        print("|           |")
        print("|")
        print("|")
        print("|")
        print("|")
    elif chances == 4:
        print("-------------")
        print("|           |")
        print("|           O")
        print("|           |")
        print("|          /")
        print("|")
        print("|")
        print("|")
    elif chances == 3:
        print("-------------")
        print("|           |")
        print("|           O")
        print("|           |")
        print("|          / ")
        print("|")
        print("|")
        print("|")
    elif chances == 2:
        print("-------------")
        print("|           |")
        print("|           O")
        print("|           |")
        print("|          / \\")
        print("|")
        print("|")
        print("|")
    elif chances == 1:
        print("-------------")
        print("|           |")
        print("|           O")
        print("|          /|")
        print("|          / \\")
        print("|")
        print("|")
        print("|")
    elif chances == 0:
        print("-------------")
        print("|           |")
        print("|           O")
        print("|          /|\\")
        print("|          / \\")
        print("|")
        print("|")
        print("|")

        print("Que pena! Você perdeu")
        print("A palavra era ", palavra)
        break
    letra = str(input("Digite a letra: "))
    if letra in letras:
        print("Letra já escolhida!")

    letras.append(letra)
    if chances == 0:
        print("Que pena você perdeu")


    if letra in palavra:
        for indice, letter in enumerate(palavra):
            if letter == letra:
                escondida[indice] = letra
    else:
        chances -= 1

    if escondida == list(palavra):
        print("Parabéns! Você ganhou")
        print(palavra)
        break
    print('\n')


