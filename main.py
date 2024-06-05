class Gomoku:
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
      else:
          print("Posição já ocupada.")





gomoku = Gomoku()
gomoku.posicionar(3,4, "X")
gomoku.print_tabuleiro()