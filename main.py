import random


class Gomoku():
    def __init__(self, tamanho=19):
        self.tamanho = tamanho
        self.tabuleiro = []
        row = []
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                row.append("-")
            self.tabuleiro.append(row)
            row = []

    def print_tabuleiro(self):
      for row in self.tabuleiro:
        for i in row:
          print(" " + i, end="")
        print()

    def posicionar(self, row, col, x):
      row -= 1
      col -= 1
      if self.tabuleiro[row][col] == "-":
        self.tabuleiro[row][col] = x
        return True
      return False
    
    def verificarGanhador(self):
        #Horizontal check
        for row in self.tabuleiro:
            p0 = 0
            p1 = 0
            for i in row:
                if i == "X":
                    p0 += 1
                if i == "O":
                    p1 += 1
            if p0 == 5:
                return 0
            elif p1 == 5:
                return 1
        #Vertical Check
        c = 0
        p0 = 0
        p1 = 0
        while c < len(self.tabuleiro):
            r = 0
            while r < len(self.tabuleiro):
                if self.tabuleiro[r][c] == "X":
                    p0 += 1
                    p1 = 0
                    if p0 == 5:
                        return 0
                elif self.tabuleiro[r][c] == "O":
                    p0 = 0
                    p1 += 1
                    if p1 == 5:
                        return 1
                else:
                    p0 = 0
                    p1 = 0
                r += 1
            c += 1
        #Diagonal Check Up
        p0 = 0
        p1 = 0
        aux = 0
        while aux < len(self.tabuleiro):
            c = aux
            r = 0
            while c < len(self.tabuleiro):
                if self.tabuleiro[r][c] == "X":
                    p0 += 1
                elif self.tabuleiro[r][c] == "O":
                    p1 += 1
                else:
                    p0 = 0
                    p1 = 0
                if p0 == 5:
                    return 0
                elif p1 == 5:
                    return 1
                c += 1
                r += 1
            aux += 1
        #Diagonal Check Down
        aux = 1
        while aux < len(self.tabuleiro):
            r = aux
            c = 0
            while r < len(self.tabuleiro):
                if self.tabuleiro[r][c] == "X":
                    p0 += 1
                elif self.tabuleiro[r][c] == "O":
                    p1 += 1
                else:
                    p0 = 0
                    p1 = 0
                if p0 == 5:
                    return 0
                elif p1 == 5:
                    return 1
                c += 1
                r += 1
            aux += 1

        #Diagonal Check Up Invert
        aux = len(self.tabuleiro) - 1
        while aux >= 0:
            c = aux
            r = 0
            while r < len(self.tabuleiro):
                if self.tabuleiro[r][c] == "X":
                    p0 += 1
                elif self.tabuleiro[r][c] == "O":
                    p1 += 1
                else:
                    p0 = 0
                    p1 = 0
                if p0 == 5:
                    return 0
                elif p1 == 5:
                    return 1
                c -= 1
                r += 1
            aux -= 1

        #Diagonal Check Down Invert
        aux = 1
        while aux < len(self.tabuleiro):
            r = aux
            c = 4
            while r < len(self.tabuleiro):
                if self.tabuleiro[r][c] == "X":
                    p0 += 1
                elif self.tabuleiro[r][c] == "O":
                    p1 += 1
                else:
                    p0 = 0
                    p1 = 0
                if p0 == 5:
                    return 0
                elif p1 == 5:
                    return 1
                c -= 1
                r += 1
            aux += 1
        return "Continua"

        
                
    
class Game():
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        self.players = ["X", "O"]
        self.currentPlayer = 0
        self.gameEnded= False

    def switchPlayer(self):
        if self.currentPlayer == 0:
            self.currentPlayer = 1
        else:
            self.currentPlayer = 0

    def placePiece(self, row, col, player):
        if player == 0:
            self.tabuleiro.posicionar(row, col, "X")
        else:
            self.tabuleiro.posicionar(row, col, "O")

    def askInput(self):
        row = int(input(f"Jogador {self.currentPlayer}, digite a LINHA:"))
        col = int(input(f"Jogador {self.currentPlayer}, digite a COLUNA:"))
        while self.tabuleiro.tabuleiro[row-1][col-1] == self.players[self.currentPlayer]:
            print("Jogada inválida, tente novamente!")
            row = int(input(f"Jogador {self.currentPlayer}, digite a LINHA:"))
            col = int(input(f"Jogador {self.currentPlayer}, digite a COLUNA:"))
        return [row, col]


    def startPlayerGameLoop(self):
        while not self.gameEnded:
            jogada = self.askInput()
            self.placePiece(jogada[0], jogada[1], self.currentPlayer)
            self.tabuleiro.print_tabuleiro()
            ganhador = self.tabuleiro.verificarGanhador()
            if ganhador == 0:
                self.gameEnded = True
                return "Jogador 0 ganhou!"
            elif ganhador == 1:
                self.gameEnded = True
                return "Jogador 1 ganhou!"
            self.switchPlayer()

    def generateInput(self):
        row = random.randint(0, 19)
        col = random.randint(0, 19)
        while self.tabuleiro.tabuleiro[row-1][col-1] == self.players[self.currentPlayer]:
            row = random.randint(0, 19)
            col = random.randint(0, 19)
        return [row, col]

    def startBotGameLoop(self):
        while not self.gameEnded:
            if self.currentPlayer == 0:
                jogada = self.askInput()
            else:
                jogada = self.generateInput()
                print(f"BOT jogou {jogada[0]}, {jogada[1]}")
            self.placePiece(jogada[0], jogada[1], self.currentPlayer)
            self.tabuleiro.print_tabuleiro()
            ganhador = self.tabuleiro.verificarGanhador()
            if ganhador == 0:
                self.gameEnded = True
                return "Jogador 0 ganhou!"
            elif ganhador == 1:
                self.gameEnded = True
                return "Bot ganhou!"
            self.switchPlayer()

    def start(self):
        modo = int(input("Escolha seu modo de jogo:\n1 - Player 0 vs Player 1\n2 - Player vs Bot\n"))
        if modo == 1:
            return self.startPlayerGameLoop()
        elif modo == 2:
            return self.startBotGameLoop()


gomoku = Gomoku()
game = Game(gomoku)
print(game.start())