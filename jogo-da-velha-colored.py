#! -*- coding: utf-8 -*-
__author__ = 'Desnown'
__date__ = '05/2019'


from os import system, name
from termcolor import colored, cprint
from time import sleep
from pdb import set_trace

color = {'Player 1':'blue', 'Player 2':'magenta',
        'Unknown':'green', 'Velha':'red',
        'Aviso':'red'}



def clear_output():
    '''
    Limpar Tela para que fique melhor a vizualiação.
    '''
    if name == 'posix':
        system('clear')
    else:
        system('cls')


def welcome():
    ''' Função responsável por dar as boas vindas aos players.
    '''
    cprint(f"""+-------------------------------+
| Bem-Vinda(o) ao Jogo da Velha |
+-------------------------------+
| Author: {__author__}               |
| Date: {__date__}                 |
+-------------------------------+\n""", 'green', attrs=['bold'])


def rules():
    opcoes = colored('''\nVocês desejam ler as regras do jogo?''')+\
        colored('\n1) SIM', color='green', attrs=['bold'])+\
        colored('\n2) NÃO', color='red', attrs=['bold'])

    rules = colored('''
1) O tabuleiro é uma matriz de 3 linhas por 3 colunas.
2) 2 players escolhem uma marcação cada um - (X) ou (O).
3) Os players jogam alternadamente,numa lacuna que esteja vazia.
4) O objetivo é conseguir três círculos ou três xis na horizontal, vertical ou diagonal.                      
5) Quando um jogador conquista o objetivo, costuma-se riscar os três símbolos.\n''', color='green') +\
        colored('''
AS REGRAS SERÃO EXIBIDAS DURANTE 10 SEGUNDOS.
''', color='white', attrs=['bold', 'dark', 'blink'])+\
        colored('''
CASO QUEIRA PULAR ESTA ETAPA, PRESSIONE AS SEGUINTES TECLAS: CTRL C''', color='white', attrs=['bold', 'dark'])



    while True:
        try:
            while True:
                try:
                    cprint(opcoes)
                    rules_info = int(input('>: '))
                    break

                except:
                    clear_output()
                    sleep(1)

            if rules_info == 1:
                clear_output()
                cprint(rules)
                sleep(10)
                break

            else:
                break

        except KeyboardInterrupt:
            clear_output()
            cprint("PULANDO ETAPA...", 'red', attrs=['bold'])
            sleep(.5)
            break


def display_board(tab=[' ']*9, jog='Unknown'):
    '''
    Função responsável por printar o jogo na tela.
    '''

    if len(tab) != 9:
        cprint("Só aceitamos 9 posições", color='red', attrs=['bold','dark'])
        exit()

    cprint(f'''  {tab[0]} | {tab[1]} | {tab[2]}  
-------------
  {tab[3]} | {tab[4]} | {tab[5]}  
-------------
  {tab[6]} | {tab[7]} | {tab[8]} 
''', color[jog], attrs=['bold'])


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
    Função que "carimba" o 'maker' no lugar que o player pediu.
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
    Retorna um valor booleano(True) caso a posição requisitada esteja vazia
    '''

    return tab[position-1] == ' '


def full_board_check(tab):
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
        try:
            pos = int(input(f"{jog}, qual posição que você deseja(1-9)\n>: "))
            if pos in range(1,10):
                if not space_check(tab, pos):
                    clear_output()
                    cprint(f"POSIÇÃO {pos} ESTÁ OCUPADA", color=color['Aviso'], attrs=['dark'])
                    display_board(tabuleiro, jog)
                else:
                    return pos
        except ValueError:
                cprint('\nSOMENTE NÚMEROS!!!', color='white')

        else:
            print("\nPosição fora do alcance.")


def print_points(pontos_jogadores):
    '''Printa os pontos dos jogadores do jogo'''

    cprint(f'''+----------------+
|  Player 1 : {pontos_jogadores["Player 1"]}  |
+----------------+
|  Player 2 : {pontos_jogadores["Player 2"]}  |
+----------------+\n''', color='white', attrs=['bold'])


def replay():
    '''
    Função responsável por solicitação de um novo jogo, ou não
    '''

    #OBS: Obedecendo a PEP 8 de no máximo 79 caracteres de comprimento
    return [cprint(colored('Vocês desejam jogar novamente?\n') +
        colored('1) SIM\n', color='green', attrs=['bold']) +
        colored('QUALQUER TECLA P/ NÃO', color='red', attrs=['dark', 'bold'])),

        input('>: '),clear_output()]


def printing_exit():
    '''Printa na tela que o jogo está sendo fechado.'''
    cprint("SAINDO DO JOGO...", 'red', attrs=['bold'])
    sleep(1)
    clear_output()

try:
    clear_output()
    welcome()
    pontos = {'Player 1': 0, 'Player 2': 0}#Guardar os pontos de cada um
    player1_marker, player2_marker = player_input() #Player escola X ou O
    player_1 = 'Player 1' #Jogador primario
    player_2 = 'Player 2' #Jogador secundário
    prim_jogada = True

except KeyboardInterrupt:
    clear_output()
    printing_exit()
    exit()

rules()


while True:
    tabuleiro = [' '] * 9 #Tabuleiro(list) com 9 espaços.
    game_on = True #Mantenha o jogo percorrendo.

    try:
        while game_on:
            clear_output()
            display_board(tabuleiro, player_1)

            if player_1 == 'Player 1':
                position = player_choice(tabuleiro, player_1)
                place_marker(tabuleiro,player1_marker, position)

            else:
                position = player_choice(tabuleiro, player_1)
                place_marker(tabuleiro,player1_marker, position)

            if win_check(tabuleiro, player1_marker):
                clear_output()
                cprint(f"{player_1.upper()} GANHOU!!!", color=color[player_1], attrs=['blink', 'bold'])
                pontos[player_1]+=1
                print_points(pontos)
                display_board(tabuleiro, player_1)
                game_on = False

            else:
                if full_board_check(tabuleiro):
                    clear_output()
                    cprint("   WE TIED!  ", attrs=['blink'])
                    display_board(tabuleiro, 'Velha')
                    break

            #ATRIBUIÇÃO SIMULTÂNEA
            player_1, player_2 = player_2, player_1 
            player1_marker, player2_marker = player2_marker, player1_marker

        if replay()[1] != '1':
            clear_output()
            printing_exit()
            break

        else:
            player_1, player_2 = player_2, player_1
            player1_marker, player2_marker = player2_marker, player1_marker
            cprint("RECOMEÇANDO...", 'yellow', attrs=['bold'])
            sleep(1)
            cprint('OBS: PLAYER GANHADOR É QUEM COMEÇA!', 'yellow', attrs=['bold'])
            sleep(3)
    except KeyboardInterrupt:
        printing_exit()
        break
