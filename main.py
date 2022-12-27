import sys

from PyQt5.QtWidgets import QApplication
from Widgets.Sections.MainWindow import MainWindow

if __name__=='__main__':
    app = QApplication(sys.argv)
    simulator = MainWindow()

    app.exec_()