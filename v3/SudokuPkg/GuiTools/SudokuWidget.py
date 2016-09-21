import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

from .SudokuCell import SudokuCellClass
from .SudokuGroup import SudokuGroupClass
from .SudokuLine import SudokuLineClass

class SudokuWidgetClass(pysidegui.QWidget):
    def __init__(self, filename, parent=None):
        super().__init__(parent)
        self.setup()
        if filename != None:
            self.fillCells(filename)

    def setup(self):
        mainBox = pysidegui.QGridLayout()

        self.cells = []
        for i in range(0,9):
            row = []
            for j in range(0,9):
                cell = SudokuCellClass(i, j)
                row.append(cell)
                # mainBox.addWidget(cell,i,j)
            self.cells.append(row)

        self.groups = []
        for i in range(0,3):
            row = []
            for j in range(0,3):
                group = SudokuGroupClass(i, j, [row[j*3+0:j*3+3] for row in self.cells[i*3+0:i*3+3]])
                row.append(group)
                mainBox.addWidget(group, i, j)
            self.groups.append(row)

        # print([r[1].coor for r in cells])

        self.rows = []
        for row in range(0,9):
            line = SudokuLineClass([r for r in self.cells[row]])
            self.rows.append(line)

        self.cols = []
        for col in range(0,9):
            line = SudokuLineClass([r[col] for r in self.cells])
            self.cols.append(line)

        mainBox.setSpacing(0)

        buttonBox = pysidegui.QHBoxLayout()

        solveButton = pysidegui.QPushButton("Solve")
        solveButton.clicked.connect(self.solve)

        buttonBox.addWidget(solveButton)

        # dfsButton = pysidegui.QPushButton("DFS")
        # dfsButton.clicked.connect(self.dfs)

        # buttonBox.addWidget(dfsButton)

        solveButton = pysidegui.QPushButton("Reset Puzzle")
        solveButton.clicked.connect(self.reset)

        buttonBox.addWidget(solveButton)

        mainBox.addLayout(buttonBox, 3, 0, 1, 3)

        self.setLayout(mainBox)
        self.count = 0

    def dfs(self):
        # print(self.count); self.count += 1

        if self.isFinished():
            return True

        cell = self.firstEmptyCell()
        # print(cell.getCoors())

        import copy
        cell_poss = copy.deepcopy(cell.possibleVals[:])

        # print(cell_poss)
        cell.possibleVals = [1,2,3,4,5,6,7,8,9]
        while len(cell.possibleVals):
            move = cell.possibleVals.pop()

            cell_poss = copy.deepcopy(cell.possibleVals[:])

            # print("Move: " + str(move))
            if cell.setValue(move):
                # print("Value set: " + str(move))
                if self.dfs():
                    return True
                else:
                    cell.undo(cell_poss)

        cell.undo()

        return False


    def firstEmptyCell(self):
        succ = []
        for row in self.cells:
            for cell in row:
                if not cell.value:
                    return cell

    def solve(self):
        finished = False
        unsolvableC = 0
        import time
        start = time.clock()
        while (not finished and unsolvableC < 3):
            changed = False
            for row in self.groups:
                for group in row:
                    changed |= group.eliminateChoices()
                    changed |= group.checkSingularities()
            for line in self.rows:
                changed |= line.eliminateChoices()
                changed |= line.checkSingularities()
            for line in self.cols:
                changed |= line.eliminateChoices()
                changed |= line.checkSingularities()

            if self.isFinished():
                finished = True
            if not changed:
                unsolvableC += 1
            else:
                unsolvableC = 0
        if (unsolvableC >= 2):
            print("Switching to DFS!")
            self.dfs()
        if (finished):
            print("Finished!")
        if (self.verifyCurrentBoard()):
            print("Verified!")
        end = time.clock()
        print("Time taken: " + str(end - start) + " seconds")

    def isFinished(self):
        sum = 0
        for row in self.cells:
            for cell in row:
                sum += cell.numPossibilities()
        return not sum

    def reset(self):
        for rows in self.cells:
            for cell in rows:
                cell.reset()

    # TODO: Better way to do this
    def fillCells(self, filename):
        givens = dict()
        for i in range(1,10):
            givens[i] = []
        file = open(filename)
        for line in file:
            self.cells[int(line[1])][int(line[3])].setGiven(int(line[6]))

    def verifyCurrentBoard(self):
        for row in self.groups:
            for group in row:
                if not group.verify():
                    return False
        for line in self.rows:
            if not line.verify():
                return False
        for line in self.cols:
            if not line.verify():
                return False
        return True

    def validMove(self, cell, newVal):
        for row in self.groups:
            for group in row:
                if cell in group.cells:
                    for ocell in group.cells:
                        if ocell.value == newVal:
                            return False
        for line in (self.rows + self.cols):
            if cell in line.cells:
                for ocell in line.cells:
                    if ocell.value == newVal:
                        return False
        return True