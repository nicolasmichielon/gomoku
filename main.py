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
        p0 = 0
        p1 = 0
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
        r = 0
        p0 = 0
        p1 = 0
        aux = 0
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
        return "Continua"
    #Diagonal Check
        
                
    
class Game():
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        self.players = ["X", "O"]
        self.currentPlayer = 0

gomoku = Gomoku()
gomoku.posicionar(3,4, "X")
gomoku.posicionar(3,5, "O")
gomoku.posicionar(3,6, "O")
gomoku.posicionar(3,7, "X")
gomoku.posicionar(3,8, "O")
gomoku.posicionar(4,8, "O")
gomoku.posicionar(5,8, "O")
gomoku.posicionar(6,8, "O")
gomoku.posicionar(7,8, "O")
gomoku.posicionar(3,9, "O")
gomoku.print_tabuleiro()
print(gomoku.verificarGanhador())