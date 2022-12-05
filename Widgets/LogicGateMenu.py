from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class LogicGateMenu(QWidget):
    def __init__(self, parentWindow):
        super(LogicGateMenu, self).__init__()

        vbox = QVBoxLayout()

        button = QPushButton("INPUT")
        button.clicked.connect(lambda: self.createLogicGate("INPUT_STREAM"))
        vbox.addWidget(button)

        button = QPushButton("AND")
        button.clicked.connect(lambda: self.createLogicGate("AND"))
        vbox.addWidget(button)

        button = QPushButton("OR")
        button.clicked.connect(lambda: self.createLogicGate("OR"))
        vbox.addWidget(button)

        button = QPushButton("XOR")
        button.clicked.connect(lambda: self.createLogicGate("XOR"))
        vbox.addWidget(button)

        self.setLayout(vbox)
        self.parentWindow = parentWindow

    def createLogicGate(self, type):
        self.parentWindow.logicGateContainer.addGate(type)
