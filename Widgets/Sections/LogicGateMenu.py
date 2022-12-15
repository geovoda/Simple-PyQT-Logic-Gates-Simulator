from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5 import QtGui
from PyQt5 import QtCore

from Widgets.Buttons.GateButton import GateButton


class LogicGateMenu(QWidget):
    def __init__(self, parentWindow):
        super(LogicGateMenu, self).__init__()

        vbox = QVBoxLayout()

        button = QPushButton("INPUT")
        button.clicked.connect(lambda: self.createLogicGate("INPUT_STREAM"))
        vbox.addWidget(button)

        button = QPushButton("OUTPUT")
        button.clicked.connect(lambda: self.createLogicGate("OUTPUT_STREAM"))
        vbox.addWidget(button)

        button = GateButton("AND", self)
        button.connect(lambda: self.createLogicGate("AND"))
        vbox.addWidget(button)

        button = GateButton("NAND", self)
        button.connect(lambda: self.createLogicGate("NAND"))
        vbox.addWidget(button)

        button = GateButton("OR", self)
        button.connect(lambda: self.createLogicGate("OR"))
        vbox.addWidget(button)

        button = GateButton("NOR", self)
        button.connect(lambda: self.createLogicGate("NOR"))
        vbox.addWidget(button)

        button = GateButton("XOR", self)
        button.connect(lambda: self.createLogicGate("XOR"))
        vbox.addWidget(button)

        button = GateButton("XNOR", self)
        button.connect(lambda: self.createLogicGate("XNOR"))
        vbox.addWidget(button)

        self.setLayout(vbox)
        self.parentWindow = parentWindow

    def createLogicGate(self, type):
        self.parentWindow.logicGateContainer.addGate(type)
