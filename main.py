from PyQt5.QtWidgets import QApplication
from Widgets.SimulatorWindow import MainWindow

if __name__=='__main__':
    app = QApplication([])
    simulator = MainWindow()
    app.exec_()