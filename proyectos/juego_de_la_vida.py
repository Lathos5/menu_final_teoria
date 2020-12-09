import copy
import random
import itertools
import time
import os


class GameOfLife(object):

    def __init__(self, rows:int, cols:int, percent:float, FirstGen:bool):

        self.rows = rows
        self.cols = cols
        self.percent = round(percent)
        self.FirstGen = FirstGen

        aux_ones = 0

        self.cells = []

        for n in range (0, (self.rows*self.cols)):
            if aux_ones != self.percent:
                self.cells.append(1)
                aux_ones += 1
            else:
                self.cells.append(0)
        
        random.shuffle(self.cells)
        print("PRIMERA GENERACIÓN:")
        print(self.cells)
        print("*"*50)
        #row_life = lambda: [cells[random.randint(0,len(cells))] for n in range(self.cols)]
        if self.FirstGen:
            row_life = lambda: [self._returnCell() for n in range(self.cols)]
            self.game = [row_life() for n in range(self.rows)]

            self.FirstGen = False
        else:
            row_life = lambda: [random.randint(0,1) for n in range(self.cols)]
            self.game = [row_life() for n in range(self.rows)]

        self.life = 1
        self.dead = 1

    def _returnCell(self) -> int:

        aux = random.randint(0,len(self.cells)-1)
        tempCell = self.cells[aux]

        self.cells.pop(aux)        

        return tempCell


    def __str__(self):

        table = ''
        for row in self.game:
            for cell in row:
                table += '@ ' if cell else '. '

            table += '\n'

        table += "Life: {0} Dead: {1}".format(self.life, self.dead)
        return table

    def evaluate(self, row, col):

        distance = list(set(itertools.permutations([-1, -1, 1, 1, 0], 2)))
        into_table = lambda x, y: (x in range(self.rows) and y in range(self.cols))

        total = 0
        for r, c in distance:
            if into_table(r + row, c + col):
                total += self.game[r + row][c + col]
        return total

    def test(self):

        gameaux = copy.deepcopy(self.game)
        self.life = 0
        self.dead = 0

        for r in range(self.rows):
            for c in range(self.cols):
                total = self.evaluate(r, c)

                if (total < 2 or total > 3) and gameaux[r][c]:
                    gameaux[r][c] = 0
                    self.dead += 1
                elif total == 3 and not gameaux[r][c]:
                    gameaux[r][c] = 1
                    self.life += 1

        self.game = copy.deepcopy(gameaux)

