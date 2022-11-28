from PyQt5.QtWidgets import QApplication
from Widgets.SimulatorWindow import MainWindow

app = QApplication([])
simulator = MainWindow()
app.exec_()
