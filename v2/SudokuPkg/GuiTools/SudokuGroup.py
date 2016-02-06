import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

from .SudokuCell import SudokuCellClass

class SudokuGroupClass(pysidegui.QFrame):
    def __init__(self, x, y, cells, parent=None):
        super().__init__(parent)
        self.cells = cells
        self.coor = (x, y)
        self.setup()

    def setup(self):

        mainBox = pysidegui.QGridLayout()

        for i in range(0,3):
            for j in range(0,3):
                mainBox.addWidget(self.cells[i][j],i,j)

        mainBox.setSpacing(0)
        mainBox.setContentsMargins(0,0,0,0)

        self.setLayout(mainBox)
        self.setFrameStyle(pysidegui.QFrame.Panel)

        # self.setText(str(self.coor))
        # self.setFixedSize(40,40)
        # self.setReadOnly(True)
        # self.setSizePolicy(pysidegui.QSizePolicy.Expanding,pysidegui.QSizePolicy.Preferred)
        # self.setAlignment(pysidecore.Qt.AlignHCenter)

    def eliminateChoices(self):
        print("Elimating choices in groups.")
        linearCells = []
        for row in self.cells:
            linearCells += row
        for cell in linearCells:
            if not cell.numPossibilities():
                continue
            if cell.numPossibilities() == 1:
                cell.setValue()
            else:
                for otherCells in linearCells:
                    if cell.getCoors() == otherCells.getCoors():
                        continue
                    else:
                        if otherCells.value != None:
                            cell.removePossibility(otherCells.value)
            if cell.numPossibilities() == 1:
                cell.setValue()

    def checkSingularities(self):
        print("Finding singularities in groups.")
        linearCells = []
        for row in self.cells:
            linearCells += row
        counts = {}
        for i in range(1,10):
            counts[i] = 0
        for cell in linearCells:
            for num in cell.possibilities():
                if counts[num] == 0:
                    counts[num] = cell
                else:
                    counts[num] = None
        for key, value in counts.items():
            if type(value) == SudokuCellClass:
                print(value.coor)
                print(key)
                value.setValue(key)
                self.eliminateChoices()

    def verify(self):
        linearCells = []
        for row in self.cells:
            linearCells += row
        count = {}
        for i in range(1, 10):
            count[i] = 0
        for cell in linearCells:
            if cell.value != None:
                count[cell.value] += 1
        for key, val in count.items():
            if val > 1:
                print(count)
                return False
        return True
