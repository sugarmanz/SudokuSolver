
from .SudokuCell import SudokuCellClass

class SudokuLineClass(object):

    def __init__(self, cells):
        super().__init__()
        self.cells = cells

    def eliminateChoices(self):
        changes = False
        # print("Elimating choices in rows.")
        for cell in self.cells:
            if not cell.numPossibilities():
                continue
            if cell.numPossibilities() == 1:
                cell.setValue()
                changes = True
            else:
                for otherCells in self.cells:
                    if cell.getCoors() == otherCells.getCoors():
                        continue
                    else:
                        if otherCells.value != None:
                            changes |= cell.removePossibility(otherCells.value)
            if cell.numPossibilities() == 1:
                cell.setValue()
                changes = True
        count = 0
        unsetCells = []
        setValues = []
        for cell in self.cells:
            if cell.value == None:
                count += 1
                unsetCells.append(cell)
            else:
                setValues.append(cell.value)
        if count > 5:
            group = unsetCells[0].group
            for cell in unsetCells:
                if cell.group != group:
                    return changes
            # Else
            for cell in group:
                if cell not in self.cells:
                    for value in (set([1,2,3,4,5,6,7,8,9]) - set(setValues)):
                        changes |= cell.removePossibility(value)

        return changes

    def checkSingularities(self):
        # print("Finding singularities in groups.")
        counts = {}
        changes = False
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
                # print(value.coor)
                # print(key)
                # input()
                value.setValue(key)
                self.eliminateChoices()
                changes = True
                
        return changes

    def verify(self):
        count = {}
        for i in range(1, 10):
            count[i] = 0
        for cell in self.cells:
            if cell.value != None:
                count[cell.value] += 1
        for key, val in count.items():
            if val > 1:
                # print(count)
                return False
        return True