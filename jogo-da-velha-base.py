#! -*- coding: utf-8 -*-
__author__ = 'Desnown'
__date__ = '02/2019'


from os import system, name
from time import sleep

def clear_output():
    '''
    Limpar Tela para que fique melhor a vizualiação.
    '''

    if name == 'posix':
        system('clear')
    else:
        system('cls')


def display_board(tab=[' ']):
    '''
    Função responsável por printar o jogo na tela.
    '''

    if len(tab) != 9:
        print("Só aceitamos 9 posições")
        exit()

    print(f'''  {tab[0]} | {tab[1]} | {tab[2]}  
-------------
  {tab[3]} | {tab[4]} | {tab[5]}  
-------------
  {tab[6]} | {tab[7]} | {tab[8]} 
''')


def player_input():
    '''
    Função responsável por solicitar "X" ou "O" do primeiro player.
    '''

    market = ''
    while market is not ('X' or 'O'):
        market = input('Qual vc prefere, X ou O\n>: ').upper()

        if market == "X":
            return ('X', 'O')
        elif market == 'O':
            return ('O', 'X')
        else:
            continue


def place_marker(tab,marker, position):
    '''
    Função que "carimba" no lugar que o player pediu.
    '''

    if tab[position-1] == ' ':
        tab[position-1] = marker


def win_check(tab, mark):
    '''
    Função responsável por verificar se o player que acabou de jogar
    ganhou a partida.
    '''

    return ((tab[0] == tab[1] == tab[2] == mark)  or
            (tab[3] == tab[4] == tab[5] == mark)  or
            (tab[6] == tab[7] == tab[8] == mark)  or
            # ->> Horizontal

            (tab[0] == tab[3] == tab[6] == mark)  or
            (tab[1] == tab[4] == tab[7] == mark)  or
            (tab[2] == tab[5] == tab[8] == mark)  or
            # ->> Vertical

            (tab[0] == tab[4] == tab[8] == mark)  or
            (tab[2] == tab[4] == tab[6] == mark)
            # ->> Diagonal
            )


def space_check(tab, position):
    '''
    Retorna um valor booleano caso a posição requisitada esteja vazia.
    '''

    return tab[position-1] == ' '


def full_board_check(tab):
    '''Diz se o tabuleiro(tab) foi ocupado'''
    for i in range(0,10):
        if space_check(tab, i):
            return False
    return True


def player_choice(tab, jog):
    '''
    Escolher a posição onde o usuário quer jogar.
    '''

    pos = 0
    while True:
        pos = int(input(f"{jog}, qual posição que você deseja(1-9)\n>: "))
        if pos in range(1,10):
            if not space_check(tab, pos):
                clear_output()
                print(f"POSIÇÃO {pos} ESTÁ OCUPADA")
                display_board(tabuleiro)
            else:
                return pos
        else:
            continue


def print_points(pontos_jogadores):
    '''Printa os pontos dos jogadores do jogo'''

    print(f'''+----------------+
|  Player 1 : {pontos_jogadores["Player 1"]}  |
+----------------+
|  Player 2 : {pontos_jogadores["Player 2"]}  |
+----------------+\n''')


def replay():
    '''
    Função responsável por solicitação de um novo jogo, ou não
    '''

    #OBS: Obedecendo a PEP 8 de no máximo 79 caracteres de comprimento
    return [print('''Vocês desejam jogar novamente?
1) SIM
2) NÃO'''),input('\n>: '),clear_output()]


try:
    clear_output()
    pontos = {'Player 1': 0, 'Player 2': 0} #Guarda os pontos de cada um
    player1_marker, player2_marker = player_input()
    player_1 = 'Player 1' #Jogador primário
    player_2 = 'Player 2' #Jogador secundário
    prim_jogada = True

except KeyboardInterrupt:
    clear_output()
    exit()


while True:
    tabuleiro = [' '] * 9 #Tabuleiro(list) com 9 espaços.
    game_on = True #Mantenha o jogo percorrendo.

    try:
        while game_on:
            clear_output()
            display_board(tabuleiro)

            if player_1 == 'Player 1':
                position = player_choice(tabuleiro, player_1)
                place_marker(tabuleiro,player1_marker, position)
            else:
                position = player_choice(tabuleiro, player_1)
                place_marker(tabuleiro,player1_marker, position)

            if win_check(tabuleiro, player1_marker):
                clear_output()
                print(f"{player_1.upper()} GANHOU!!!")
                pontos[player_1]+=1
                print_points(pontos)
                display_board(tabuleiro)
                game_on = False

            else:
                if full_board_check(tabuleiro):
                    clear_output()
                    print("{:^14}".format('WE TIED!'))
                    display_board(tabuleiro)
                    break

            #ATRIBUIÇÃO SIMULTÂNEA
            player_1, player_2 = player_2, player_1 
            player1_marker, player2_marker = player2_marker, player1_marker

        if replay()[1] != '1':
            clear_output()
            break

        else:
            player_1, player_2 = player_2, player_1
            player1_marker, player2_marker = player2_marker, player1_marker
            print("RECOMEÇANDO...")
            sleep(1)
            print('OBS: PLAYER GANHADOR DA PARTIDA PASSADA É QUEM COMEÇA!')
            sleep(3)
    except KeyboardInterrupt:
        clear_output()
        break
