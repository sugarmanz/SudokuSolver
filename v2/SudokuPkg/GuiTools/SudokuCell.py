from random import randint

import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui


class SudokuCellClass(pysidegui.QLineEdit):

    def __init__(self, x, y, parent=None):
        super().__init__(parent)
        self.coor = (x, y)
        self.setup()

    def setup(self):
        # line = pysidegui.QLineEdit(str(randint(0,9)))
        # line.setFixedSize(40,40)
        # line.setReadOnly(True)
        # line.setSizePolicy(pysidegui.QSizePolicy.Expanding,pysidegui.QSizePolicy.Preferred)
        # line.setAlignment(pysidecore.Qt.AlignHCenter)
        #
        # mainBox = pysidegui.QHBoxLayout()
        # mainBox.addWidget(line)
        #
        # self.setLayout(mainBox)
        # self.setSizePolicy(pysidegui.QSizePolicy.Expanding,pysidegui.QSizePolicy.Preferred)
        self.setText(" ")
        self.setMinimumSize(40,40)
        self.setSizePolicy(pysidegui.QSizePolicy.Minimum,pysidegui.QSizePolicy.Minimum)
        self.setReadOnly(True)
        self.setSizePolicy(pysidegui.QSizePolicy.Expanding,pysidegui.QSizePolicy.Preferred)
        self.setAlignment(pysidecore.Qt.AlignHCenter)

        self.given = False
        self.value = None
        self.possibleVals = [1,2,3,4,5,6,7,8,9]

    def setGiven(self, value):
        self.setValue(value)
        self.given = True

    def setValue(self, value=None):
        if self.given:
            print("ERROR: CAN'T CHANGE GIVEN")
            return

        if self.value != None:
            return

        if value == None:
            if self.numPossibilities() != 1:
                print("ERROR: CAN'T FIND VALUE TO SET")
                input()
                return
            value = self.possibleVals.pop()

        elif value not in self.possibleVals:
            print("WARNING: MOVE IS NOT RECOMMENDED")
            return

        if not self.parent().parent().validMove(self, value):
            print("ERROR: INVALID MOVE")
            return

        self.value = value
        self.possibleVals = []
        self.setText(str(self.value))
        self.parent().parent().verifyCurrentBoard()
        pysidecore.QCoreApplication.processEvents()
        # if not self.given:
        #     input("YAY!")

    def numPossibilities(self):
        return len(self.possibleVals)

    def possibilities(self):
        return self.possibleVals

    def removePossibility(self, val):
        try:
            self.possibleVals.remove(val)
        except ValueError:
            pass
        print(self.coor)
        print(self.possibleVals)
        if len(self.possibleVals) == 1:
            self.setValue()

    def getCoors(self):
        return self.coor;

    def reset(self):
        if not self.given:
            self.value = None
            self.setText(" ")
            self.possibleVals = [1,2,3,4,5,6,7,8,9]