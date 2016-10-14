import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

from .SudokuWidget import SudokuWidgetClass


class MainWindowClass(pysidegui.QMainWindow):

   def __init__(self, filename, parent=None):
      super().__init__(parent)
      self.setup(filename)

   def setup(self, filename):
      # Menu
      self.constructMenu()

      # Central widget
      centralWidget = SudokuWidgetClass(filename)
      self.setCentralWidget(centralWidget)

      # Misc
      self.setWindowTitle("Sudoku Solver")
      self.setWindowIcon(pysidegui.QIcon("sudoku/GuiTools/icon_circ.png"))
      self.resize(self.centralWidget().width(), self.centralWidget().height())
      
      # Show
      self.show()

   def constructMenu(self):
      exitAction = pysidegui.QAction('Exit',self)
      exitAction.setStatusTip('Exit Sudoku Solver.')
      exitAction.triggered.connect(self.close)

      newPuzzleAction = pysidegui.QAction('New Puzzle', self)
      newPuzzleAction.setStatusTip('Create new puzzle.')
      newPuzzleAction.triggered.connect(self.newPuzzle)

      loadPuzzleAction = pysidegui.QAction('Load Puzzle',self)
      loadPuzzleAction.setStatusTip('Load another Puzzle.')
      loadPuzzleAction.triggered.connect(self.loadPuzzle)

      savePuzzleAction = pysidegui.QAction('Save Puzzle',self)
      savePuzzleAction.setStatusTip('Save Puzzle To Filesystem.')
      savePuzzleAction.triggered.connect(self.savePuzzle)

      menuBar = self.menuBar()
      fileMenu = menuBar.addMenu("File")

      fileMenu.addAction(newPuzzleAction)
      fileMenu.addAction(loadPuzzleAction)
      fileMenu.addAction(savePuzzleAction)
      fileMenu.addAction(exitAction)

   def newPuzzle(self):
      pass

   def loadPuzzle(self):
      pass

   def savePuzzle(self):
      pass