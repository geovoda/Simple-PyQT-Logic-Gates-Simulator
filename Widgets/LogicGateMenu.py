from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class LogicGateMenu(QWidget):
    def __init__(self, parentWindow):
        super(LogicGateMenu, self).__init__()

        vbox = QVBoxLayout()

        for i in range(5):
            button = QPushButton("AND")
            button.clicked.connect(self.createLogicGate)
            vbox.addWidget(button)

        self.setLayout(vbox)
        self.parentWindow = parentWindow

    def createLogicGate(self):
        self.parentWindow.logicGateContainer.addGate()
