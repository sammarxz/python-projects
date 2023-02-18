import os
import random

class TicTacToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print("")
        print(f"  {self.board[0][0]}  |  {self.board[0][1]}  |  {self.board[0][2]}  ")
        print("-----------------")
        print(f"  {self.board[1][0]}  |  {self.board[1][1]}  |  {self.board[1][2]}  ")
        print("-----------------")
        print(f"  {self.board[2][0]}  |  {self.board[2][1]}  |  {self.board[2][2]}  ")
        print("")
    
    def reset(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def check_win_or_draw(self):
        dict_win = {}

        for i in ["X", "O"]:
            # Horizontals
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            # Verticals
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

            # Diagonals
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]

        if dict_win["X"]:
            self.done = "X"
            print("X Venceu")
            return "X"
        elif dict_win["O"]:
            self.done = "O"
            print("O Venceu")
            return "O"

        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != " ":
                    c += 1
                    break
        
        if c == 0:
            self.done = "D"
            print("Empate")
            return "D"

    def get_player_move(self):
        invalid_move = True

        while invalid_move:
            try:
                print("Digite a linha do seu próximo lance: ")
                x = int(input())

                print("Digite a coluna do seu próximo lance: ")
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print("Cordenadas inválidas")
                
                if self.board[x][y] != " ":
                    print("Posição já preenchida")
                    continue
            except Exception as e:
                print(e)
                continue
            invalid_move = False
        self.board[x][y] = "X"

    def bot_move(self):
        possible_moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    possible_moves.append((i, j))

        if len(possible_moves) > 0:
            for move in possible_moves:
                for letter in ["O", "X"]:
                    x, y = move
                    self.board[x][y] = letter
                    if self.check_win_or_draw() == "O":
                        self.board[x][y] = "O"
                    else:
                        self.board[x][y] = " "
            x, y = random.choice(possible_moves)
            self.board[x][y] = "O"
            # for i in possible_moves:
            #     for letter in ["O", "X"]:
            #         x, y = i
            #         self.board[x][y] = letter
            #         self.print_board()
                # self.board[x][y] = "O"

                # if self.check_win_or_draw(self.board) == "D":
                #     self.board[x][y] = "O"


        # if len(possible_moves) > 0:
        #     x, y = random.choice(possible_moves)
        #     score = self.minimax()
        #     print(score)
        #     if score > best_score:
        #         best_score = score
        #         self.board[x][y] = "O"

game = TicTacToe()
next = 0

while next == 0:
    os.system("clear")
    game.print_board()
    while game.done == "":
        game.get_player_move()
        game.bot_move()
        os.system("clear")
        game.print_board()
        # game.check_win_or_draw()

    print("Digite q para sair do jogo ou qualquer tecla para jogar novamente")
    next = input()

    if next == "q":
        break
    else:
        game.reset()
        next = 0
