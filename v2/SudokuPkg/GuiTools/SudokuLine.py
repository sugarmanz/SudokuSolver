
from .SudokuCell import SudokuCellClass

class SudokuLineClass(object):

    def __init__(self, cells):
        super().__init__()
        self.cells = cells

    def eliminateChoices(self):
        print("Elimating choices in rows.")
        for cell in self.cells:
            if not cell.numPossibilities():
                continue
            if cell.numPossibilities() == 1:
                cell.setValue()
            else:
                for otherCells in self.cells:
                    if cell.getCoors() == otherCells.getCoors():
                        continue
                    else:
                        if otherCells.value != None:
                            cell.removePossibility(otherCells.value)
            if cell.numPossibilities() == 1:
                cell.setValue()

    def checkSingularities(self):
        print("Finding singularities in groups.")
        counts = {}
        for i in range(1,10):
            counts[i] = 0
        for cell in self.cells:
            for num in cell.possibilities():
                if counts[num] == 0:
                    counts[num] = cell
                else:
                    counts[num] = None
        for key, value in counts.items():
            if type(value) == SudokuCellClass:
                print(value.coor)
                print(key)
                # input()
                value.setValue(key)
                self.eliminateChoices()

    def verify(self):
        count = {}
        for i in range(1, 10):
            count[i] = 0
        for cell in self.cells:
            if cell.value != None:
                count[cell.value] += 1
        for key, val in count.items():
            if val > 1:
                print(count)
                return False
        return True