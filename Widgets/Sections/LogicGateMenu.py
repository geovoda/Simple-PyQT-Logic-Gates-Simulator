from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5 import QtGui
from PyQt5 import QtCore


class LogicGateMenu(QWidget):
    def __init__(self, parentWindow):
        super(LogicGateMenu, self).__init__()

        vbox = QVBoxLayout()

        button = QPushButton("INPUT")
        button.clicked.connect(lambda: self.createLogicGate("INPUT_STREAM"))
        vbox.addWidget(button)

        button = QPushButton("AND")
        button.clicked.connect(lambda: self.createLogicGate("AND"))
        button.setIcon(QtGui.QIcon('and.png'))
        button.setIconSize(QtCore.QSize(50, 50))
        vbox.addWidget(button)

        button = QPushButton("NAND")
        button.clicked.connect(lambda: self.createLogicGate("NAND"))
        button.setIcon(QtGui.QIcon('nand.png'))
        button.setIconSize(QtCore.QSize(50, 50))
        vbox.addWidget(button)

        button = QPushButton("OR")
        button.clicked.connect(lambda: self.createLogicGate("OR"))
        button.setIcon(QtGui.QIcon('or.png'))
        button.setIconSize(QtCore.QSize(50, 50))
        vbox.addWidget(button)

        button = QPushButton("NOR")
        button.clicked.connect(lambda: self.createLogicGate("NOR"))
        button.setIcon(QtGui.QIcon('nor.png'))
        button.setIconSize(QtCore.QSize(50, 50))
        vbox.addWidget(button)

        button = QPushButton("XOR")
        button.clicked.connect(lambda: self.createLogicGate("XOR"))
        button.setIcon(QtGui.QIcon('xor.png'))
        button.setIconSize(QtCore.QSize(50, 50))
        vbox.addWidget(button)

        button = QPushButton("XNOR")
        button.clicked.connect(lambda: self.createLogicGate("XNOR"))
        button.setIcon(QtGui.QIcon('xnor.png'))
        button.setIconSize(QtCore.QSize(50, 50))
        vbox.addWidget(button)

        self.setLayout(vbox)
        self.parentWindow = parentWindow

    def createLogicGate(self, type):
        self.parentWindow.logicGateContainer.addGate(type)
