"""
Напишите игру "Крестики-нолики".
"""

import os
from random import randint


def print_board(array: [list]):
    print('|', end=' ')
    print(*range(len(array)), sep=' | ', end=' | \n')
    print('_' * 13)
    for i, line in enumerate(array):
        print('|', end=' ')
        print(*line, sep=' | ', end=f' | {i}\n')
        print('_' * 13)


def check(board, player):
    win_coord = ((0, 0, 0, 1, 0, 2), (1, 0, 1, 1, 1, 2), (2, 0, 2, 1, 2, 2), (0, 0, 1, 0, 2, 0), (1, 0, 1, 1, 2, 1),
                 (0, 2, 1, 2, 2, 2), (0, 0, 1, 1, 2, 2), (0, 2, 1, 1, 2, 0))
    for each in win_coord:
        if board[each[0]][each[1]] == board[each[2]][each[3]] == board[each[4]][each[5]] == player:
            return player
    return False


if __name__ == '__main__':
    lst = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print('Начинаем игру крестики - нолики')
    players = ['0', 'X']
    turn = randint(0, 1)
    player = players[turn]  
    print_board(lst)
    while True:
        print(f'Ходит {player}')
        row, col = [int(i) for i in input('Укажите стороку и столбец через пробел: ').split()]
        os.system('cls')
        lst[row][col] = player
        print_board(lst)
        if not check(lst, player):
            turn = not turn
            player = players[turn]
        else:
            print(f'Победили {player}')
            break

