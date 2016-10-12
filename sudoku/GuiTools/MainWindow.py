import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

from .SudokuWidget import SudokuWidgetClass


class MainWindowClass(pysidegui.QMainWindow):

    def __init__(self, filename, parent=None):
        super().__init__(parent)
        self.setup(filename)

    def setup(self, filename):
        centralWidget = SudokuWidgetClass(filename)

        self.setCentralWidget(centralWidget)
        self.resize(self.centralWidget().width(), self.centralWidget().height())
        self.show()

