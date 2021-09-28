import random
import unidecode


def carregar_palavras():
    # Carrega as palavras e escolhe uma aletoriamente
    arq = open("palavras.txt", "r", encoding="utf-8")
    texto = ''
    linhas = arq.readlines()
    for linha in linhas:
        texto = unidecode.unidecode((random.choice(linha.split(', '))))
    print('Era um vez um dragão solitário preso em um castelo. Ele sonhava diariamente sobre o dia em que\n'
          'alguem iria resgatá-lo e ele conseguiria voar livremente pelo mundo a fora. \n'
          'Em um belo dia, você estava caminhando pela floresta e ouviu vários grunhidos vindo de longe,\n'
          'como você é uma pessoa curiosa, se sentiu na necessidade de encontrar a origem destes sons.\n'
          'E claro, voce encontrou!'
          'Era o castelo em que o dragão era prisioneiro.\n'
          'Na entrada do castelo um mago te recebeu e contou a história do dragão. Você se comoveu e perguntou\n'
          'o que poderia fazer para libertar o pobre dragão.\n'
          'O mago te passou uma tarefa: Para libertar o dragão você precisa descobrir a palavra secreta que\n'
          'irá abrir a porta e libertar o dragão ...\n')
    return texto


def qnt_letras(texto):
    # Conta a quantidade de letras na palavra e fornece a dica
    qnt_letras = len(texto)
    print(f'Dica: A palavra contém ' + str(qnt_letras) + ' letras')


def chutar_palavra():
    # Input do usuário sobre qual letra ele deseja
    chance = input('Informe uma letra: ')
    return chance


def espaco(texto):
    # Coloca espaço em cada letra da palavra
    return ["_" for letra in texto]


def marcar_letra(chance, espaco, texto):
    # Marca a letra correta nos espaços
    pos = 0
    for letra in texto:
        if chance == letra:
            espaco[pos] = letra
        pos = pos + 1


def restart():
    # Reinicia ou encerra o jogo
    while True:
        reiniciar = int(input('Deseja jogar novamente?\n'
                              'SIM: Digite 1\n'
                              'NÃO: Digite 2\n'))
        if reiniciar not in [1, 2]:
            print('Escolha um valor válido')
            continue
        if reiniciar == 1:
            jogando()
        if reiniciar == 2:
            print('Que pena ! Nos vemos em uma próxima partida !')
            exit()


def jogando():
    die = 0
    palavra_secreta = carregar_palavras()
    print(palavra_secreta)
    qnt_letras(palavra_secreta)
    letras_acertadas = espaco(palavra_secreta)
    while True:
        # print(letras_acertadas)
        chute = chutar_palavra()
        if chute not in palavra_secreta:
            print('errou')
            die = die + 1
            print(die)
            print(f'Você ainda tem {7 - die} tentativas')
            if die == 5:
                while True:
                    esc = int(input('Se estiver muito dificil voce pode desistir ou iniciar um novo jogo,'
                                    'o que deseja fazer ?\n'
                                    'Continuar: Digite 1\n'
                                    'Desistir: Digite 2\n'
                                    'Novo jogo: Digite 3\n'))
                    if esc not in [1, 2, 3]:
                        print('Escolha um valor válido')
                        continue
                    if esc == 1:
                        break
                    if esc == 2:
                        exit()
                    if esc == 3:
                        jogando()
            if die == 7:
                print(f'XIIIII ... NÃO FOI DESTA VEZ !! A PALAVRA SECRETA ERA: {palavra_secreta.upper()}')
                restart()
        if chute in palavra_secreta:
            marcar_letra(chute, letras_acertadas, palavra_secreta)
            print('UHUUU ! VOCÊ ACERTOU !')
            letras_faltando = str(letras_acertadas.count('_'))
            if letras_faltando == '0':
                print(f'Essa não foi fácil heim !! MAAAAS... Você acertou ! A palavra correta'
                      f' era: {palavra_secreta.upper()}.\n'
                      f'Mas, o Mago tinha uma última tarefa a ser feita!\n'
                      f'Agora você precisa acertar a chave do cadeado da coleira do dragão ! '
                      f'Só assim irá conseguir libertá-lo.\n'
                      f'Para isso, o Mago te deu 2 tentativas. Se você não acertar em nenhuma '
                      f'delas, você irá ficar preso junto com o dragão !\n'
                      f'BOA SORTE !')
                chave()


def chave():
    fim = 0
    while True:
        x = int(input('Esta pronto?\n'
                      'SIM: Digite 1\n'
                      'NÃO: Digite 2\n'
                      'DESISTIR: Digite 3\n'
                      'NOVO JOGO: Digite 4\n'))
        if x not in [1, 2, 3, 4]:
            print('Escolha um valor válido!')
            continue
        if x == 2:
            print('Ok, estamos aguardando ...')
            continue
        if x == 3:
            exit()
        if x == 4:
            restart()
        if x == 1:
            key = random.choice(range(1, 7))
            print(key)
            if key == 3:
                finais = random.choice(('Você acertou a chave e libertou o dragão !! Parabéns !!\n'
                                        'Agora o dragão está livre para voar livremente pelo mundo!',
                                        'Você acertou a chave e libertou o dragão !! Parabéns !!\n'
                                        'Agora o dragão está livre para voar livremente pelo mundo causando o caos!'))
                print(finais)
                restart()
            if key != 3:
                fim = fim + 1
                if fim != 2:
                    print('Xi, você tem só mais uma chance !')

                if fim == 2:
                    print('Acabaram as suas chances !\n'
                          'Agora vocês está preso junto com o dragão ! ;(')
                    restart()
                continue


jogando()
