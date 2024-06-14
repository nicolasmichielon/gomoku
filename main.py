from random import randint

class Player():
    def __init__(self, simbolo):
        self.simbolo = simbolo
    

    def placePiece(self, tabuleiro, row, col):
        tabuleiro.posicionar(row, col, self.simbolo)
        return


class Bot(Player):
    def __init__(self, simbolo):
        super().__init__(simbolo)


    def placePiece(self, tabuleiro, row, col):
        return super().placePiece(tabuleiro, row, col)
    

    def generateInput(self, game):
        row = randint(0, 19)
        col = randint(0, 19)
        while game.tabuleiro.matriz[row-1][col-1] == game.players[game.currentPlayer]:
            row = randint(0, 19)
            col = randint(0, 19)
        return [row, col]


class Tabuleiro():
    def __init__(self, tamanho=19):
        self.tamanho = tamanho
        self.matriz = []
        row = []
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                row.append("-")
            self.matriz.append(row)
            row = []


    def print_tabuleiro(self):
        letra = 65
        num = 1
        print()
        print("     ",end="")
        for i in range(self.tamanho):
            print(chr(letra), end="  ")
            letra += 1
        print()
        for row in self.matriz:
            if num <= 9:
                print(f" {num}", end=" ")
            else:
                print(f"{num}", end=" ")
            for i in row:
                print(f"  {i}", end="")
            num += 1
            print()
        print()


    def posicionar(self, row, col, x):
      row -= 1
      col -= 1
      if self.matriz[row][col] == "-":
        self.matriz[row][col] = x
        return True
      return False
        
    
class Game():
    def __init__(self, tabuleiro, players, bot):
        self.tabuleiro = tabuleiro
        self.players = players
        self.bot = bot
        self.currentPlayer = 0
        self.gameEnded= False


    def switchPlayer(self):
        if self.currentPlayer == 0:
            self.currentPlayer = 1
        else:
            self.currentPlayer = 0


    def askInput(self):
        while True:
            input_player = input(f"Jogador {self.currentPlayer}, digite sua jogada no formato A1:")

            if len(input_player) >= 2 and len(input_player) <= 3:
                col = input_player[0]
                if 'A' <= col <= 'S' or 'a' <= col <= 's':
                    if 'a' <= col <= 's':
                        col = chr(ord(col) - 32)
                    
                    row_part = input_player[1:]
                    row_valid = True
                    row = 0

                    for char in row_part:
                        if '0' <= char <= '9':
                            row = row * 10 + (ord(char) - ord('0'))
                        else:
                            row_valid = False
                            break

                    if row_valid and 1 <= row <= 19:
                        col_num = ord(col) - 64
                        if self.tabuleiro.matriz[row-1][col_num-1] != self.players[1].simbolo and self.tabuleiro.matriz[row-1][col_num-1] != self.players[0].simbolo:
                            return [row, col_num]

            print("Jogada inválida, tente novamente!")


    def startPlayerGameLoop(self):
        while not self.gameEnded:
            jogada = self.askInput()
            self.players[self.currentPlayer].placePiece(self.tabuleiro, jogada[0], jogada[1])
            self.tabuleiro.print_tabuleiro()
            ganhador = self.verificarGanhador()
            if ganhador == 0:
                self.gameEnded = True
                return "Jogador 0 ganhou!"
            elif ganhador == 1:
                self.gameEnded = True
                return "Jogador 1 ganhou!"
            elif ganhador == "draw":
                self.gameEnded = True
                return "Empate!"
            self.switchPlayer()


    def startBotGameLoop(self):
        while not self.gameEnded:
            if self.currentPlayer == 0:
                jogada = self.askInput()
                self.players[self.currentPlayer].placePiece(self.tabuleiro, jogada[0], jogada[1])
            else:
                jogada = self.bot.generateInput(self)
                self.bot.placePiece(self.tabuleiro, jogada[0], jogada[1])
                print(f"BOT jogou {jogada[0]}, {jogada[1]}")
            self.tabuleiro.print_tabuleiro()
            ganhador = self.verificarGanhador()
            if ganhador == 0:
                self.gameEnded = True
                return "Jogador 0 ganhou!"
            elif ganhador == 1:
                self.gameEnded = True
                return "Bot ganhou!"
            elif ganhador == "draw":
                self.gameEnded = True
                return "Empate!"
            self.switchPlayer()

    
    def verificarGanhador(self):
        p0_simbolo = self.players[0].simbolo
        p1_simbolo = self.players[1].simbolo
        #Horizontal check
        for row in self.tabuleiro.matriz:
            p0 = 0
            p1 = 0
            for i in row:
                if i == p0_simbolo:
                    p1 = 0
                    p0 += 1
                if i == p1_simbolo:
                    p0 = 0
                    p1 += 1
            if p0 == 5:
                return 0
            elif p1 == 5:
                return 1
        #Vertical Check
        c = 0
        p0 = 0
        p1 = 0
        while c < len(self.tabuleiro.matriz):
            r = 0
            while r < len(self.tabuleiro.matriz):
                if self.tabuleiro.matriz[r][c] == p0_simbolo:
                    p0 += 1
                    p1 = 0
                    if p0 == 5:
                        return 0
                elif self.tabuleiro.matriz[r][c] == p1_simbolo:
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
        while aux < len(self.tabuleiro.matriz):
            c = aux
            r = 0
            while c < len(self.tabuleiro.matriz):
                if self.tabuleiro.matriz[r][c] == p0_simbolo:
                    p0 += 1
                    p1 = 0
                elif self.tabuleiro.matriz[r][c] == p1_simbolo:
                    p1 += 1
                    p0 = 0
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
        p0 = 0
        p1 = 0
        aux = 1
        while aux < len(self.tabuleiro.matriz):
            r = aux
            c = 0
            while r < len(self.tabuleiro.matriz):
                if self.tabuleiro.matriz[r][c] == p0_simbolo:
                    p1 = 0
                    p0 += 1
                elif self.tabuleiro.matriz[r][c] == p1_simbolo:
                    p0 = 0
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
        p0 = 0
        p1 = 0
        aux = len(self.tabuleiro.matriz) - 1
        while aux >= 0:
            c = aux
            r = 0
            while r < len(self.tabuleiro.matriz):
                if self.tabuleiro.matriz[r][c] == p0_simbolo:
                    p1 = 0
                    p0 += 1
                elif self.tabuleiro.matriz[r][c] == p1_simbolo:
                    p0 = 0
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
        p0 = 0
        p1 = 0
        aux = 1
        while aux < len(self.tabuleiro.matriz):
            r = aux
            c = 4
            while r < len(self.tabuleiro.matriz):
                if self.tabuleiro.matriz[r][c] == p0_simbolo:
                    p1 = 0
                    p0 += 1
                elif self.tabuleiro.matriz[r][c] == p1_simbolo:
                    p0 = 0
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

        r = 0
        c = 0
        #Draw Check
        while r < len(self.tabuleiro.matriz):
            while c < len(self.tabuleiro.matriz):
                if self.tabuleiro.matriz[r][c] == "-":
                    return
                c += 1
            r += 1
        return "draw"


    def start(self):
        modo = int(input("Escolha seu modo de jogo:\n1 - Player 0 vs Player 1\n2 - Player vs Bot\n"))
        if modo == 1:
            return self.startPlayerGameLoop()
        elif modo == 2:
            self.players[1] = self.bot
            return self.startBotGameLoop()


gomoku = Tabuleiro()
player1 = Player("X")
player2 = Player("O")
bot = Bot("O")
game = Game(gomoku, [player1, player2], bot)
print(game.start())