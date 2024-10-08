from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from Widgets.Buttons.GateButton import GateButton


class LogicGateMenu(QWidget):
    def __init__(self, parentWindow):
        super(LogicGateMenu, self).__init__()

        vbox = QVBoxLayout()

        button = GateButton("INPUT_ICON", self)
        button.connect(lambda: self.createLogicGate("INPUT_STREAM"))
        vbox.addWidget(button)

        button = GateButton("OUTPUT_ICON", self)
        button.connect(lambda: self.createLogicGate("OUTPUT_STREAM"))
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

        vbox.setAlignment(Qt.AlignTop)
        self.setLayout(vbox)
        self.parentWindow = parentWindow

    def createLogicGate(self, type):
        self.parentWindow.logicGateContainer.addGate(type)
