from sys import argv
from os import path

import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

from sudoku.GuiTools import MainWindow
from sudoku.Util import valid_files

@valid_files
def solvePuzzle(filename):
    print("Loading puzzle from '%s'." % filename)
    application = pysidegui.QApplication([])
    mainWindow = MainWindow.MainWindowClass(filename)
    exit(application.exec_())

def printUsage():
    print()
    print("Usage: sudokuSolver.py [inputfile]")
    print()
    print("Options:")
    print("        [inputfile] -> File to read puzzle from")

if __name__ == '__main__':
    if len(argv) == 1:
        filename = "sudoku/puzzles/puzzleEasy.txt"
    elif len(argv) == 2:
        filename = argv[1]
    else:
        printUsage()
        exit(1)

    solvePuzzle(filename)