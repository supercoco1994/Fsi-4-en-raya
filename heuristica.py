import random

def k_in_row(board, move, player, (delta_x, delta_y), k):
    x, y = move
    n = 0
    while board.get((x, y)) == ".":
        n += 1
        x, y = x + delta_x, y + delta_y
    x, y = move
    while board.get((x, y)) == ".":
        n += 1
        x, y = x - delta_x, y - delta_y
    n -= 1
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y
    x, y = move
    while board.get((x, y)) == player:
        n += 1
        x, y = x - delta_x, y - delta_y
    n -= 1
    return n >= k

def ventaja(board, move, player,):
    valor = 0
    x, y = move
    if board.get((x, y)) == player:
                if x == 3 or x == 4:
                    valor += 100
                    if x == 4:
                        valor += 150
                else:
                    valor += 50
                if y == 2 or y == 4 or y == 6:
                    valor += 50
                elif y == 3 or y == 5:
                    valor += 10
                else:
                    valor += 5
    return valor

def linea(board, move, player, k):
    return (k_in_row(board, move, player, (0, 1), k) or
            k_in_row(board, move, player, (1, 0), k) or
            k_in_row(board, move, player, (1, -1), k) or
            k_in_row(board, move, player, (1, 1), k))

def final(state):
    valor = 0
    for move, player in state.board.iteritems():
        for k in [3, 2, 1, 0]:
            if linea(state.board, move, player, k):
                if k >= 3:
                    if player == 'X':
                        valor += (1000000 + ventaja(state.board, move, player))/100
                    else:
                        valor -= (1000000 + ventaja(state.board, move, player))/10
                if k == 2:
                    if player == 'X':
                        valor += (10000 + ventaja(state.board, move, player))/50
                    else:
                        valor -= (10000 + ventaja(state.board, move, player))/5
                if k == 1:
                    if player == 'X':
                        valor += (100 + ventaja(state.board, move, player))/2
                    else:
                        valor -= (100 + ventaja(state.board, move, player))/2
                if k == 0:
                    if player == 'X':
                        valor += 40 + ventaja(state.board, move, player)
                    else:
                        valor -= 40 + ventaja(state.board, move, player)
            else:
                valor -= 70
    return valor