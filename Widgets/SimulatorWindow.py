from PyQt5.QtWidgets import QWidget, QHBoxLayout, QScrollArea
from Widgets.LogicGateContainer import LogicGateContainer
from Widgets.LogicGateMenu import LogicGateMenu


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.logicGateMenu = LogicGateMenu(self)
        self.logicGateContainer = LogicGateContainer(parent=self)

        scroll = QScrollArea()
        scroll.setWidget(self.logicGateMenu)
        scroll.setWidgetResizable(True)
        scroll.setFixedWidth(100)

        hbox = QHBoxLayout()
        hbox.addWidget(scroll)
        hbox.addWidget(self.logicGateContainer, 1)

        self.setLayout(hbox)

        self.setWindowTitle("Simulator porti logice")
        self.setGeometry(0, 0, 800, 600)

        self.show()
