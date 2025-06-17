"""
🎮 Simulación de Tic Tac Toe con IA (Minimax)

- Jugador humano: X
- IA (Minimax): O
"""

import math

# Tablero vacío
board = [' ' for _ in range(9)]

# Función para imprimir el tablero
def print_board():
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print('|'.join(row))
        if i < 2:
            print('-' * 5)

# Verificar si hay ganador
def check_winner(b, player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # filas
        [0,3,6], [1,4,7], [2,5,8],  # columnas
        [0,4,8], [2,4,6]            # diagonales
    ]
    for combo in win_combinations:
        if all(b[i] == player for i in combo):
            return True
    return False

# Verificar si el juego terminó
def is_terminal(b):
    return check_winner(b, 'X') or check_winner(b, 'O') or ' ' not in b

# Evaluar estado del tablero
def evaluate(b):
    if check_winner(b, 'O'):
        return 1
    elif check_winner(b, 'X'):
        return -1
    else:
        return 0

# Algoritmo Minimax
def minimax(b, depth, is_maximizing):
    if is_terminal(b):
        return evaluate(b)
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                eval = minimax(b, depth + 1, False)
                b[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                eval = minimax(b, depth + 1, True)
                b[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

# Movimiento de la IA
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Juego principal
def play():
    print("🎮 Bienvenido a Tic Tac Toe. Tú eres X.")
    print_board()
    
    while not is_terminal(board):
        # Turno jugador
        move = int(input("Elige una posición (0-8): "))
        if board[move] != ' ':
            print("Casilla ocupada. Intenta otra.")
            continue
        board[move] = 'X'
        print_board()

        if is_terminal(board):
            break

        # Turno IA
        print("🤖 Turno de la IA...")
        ai_move()
        print_board()

    # Resultado
    if check_winner(board, 'X'):
        print("🏆 ¡Ganaste!")
    elif check_winner(board, 'O'):
        print("💻 La IA gana.")
    else:
        print("🤝 Empate.")

# Ejecutar juego
if __name__ == "__main__":
    play()
