from sys import argv
from os import path

import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

from SudokuPkg.GuiTools import MainWindow

# NOTE: This puzzle reverses v1 file inputs.
def solvePuzzle(filename):
    if not path.isfile(filename):
        print("File: '%s' does not exist or is not a valid file." % filename)
        exit(1)
    print("Loading puzzle from '%s'." % filename)
    application = pysidegui.QApplication([])
    mainWindow = MainWindow.MainWindowClass(filename)
    exit(application.exec_())


if __name__ == '__main__':
    if len(argv) == 1:
        filename = "puzzles/puzzleEasy.txt"
    elif len(argv) == 2:
        filename = argv[1]
    else:
        print("""
Usage: sudokuSovlver.py [inputfile]

Option:
        inputfile -> File to read puzzle from and solve
""")
        exit(1)
    solvePuzzle(filename)