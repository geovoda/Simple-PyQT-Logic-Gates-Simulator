from PyQt5.QtWidgets import QWidget, QHBoxLayout, QScrollArea
from Widgets.Sections.LogicGateContainer import LogicGateContainer
from Widgets.Sections.LogicGateMenu import LogicGateMenu


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.logicGateMenu = LogicGateMenu(self)
        self.logicGateContainer = LogicGateContainer(parent=self)

        scrollableArea = QScrollArea()
        scrollableArea.setWidget(self.logicGateMenu)
        scrollableArea.setWidgetResizable(True)
        scrollableArea.setFixedWidth(84)
        scrollableArea.setStyleSheet("QScrollArea{border: none; border-right: 2px solid #c9d8ff;}")

        hbox = QHBoxLayout()
        hbox.addWidget(scrollableArea)
        hbox.addWidget(self.logicGateContainer, 1)
        hbox.setContentsMargins(0, 0, 0, 0)

        self.setLayout(hbox)

        self.setWindowTitle("Simulator porti logice")
        self.setGeometry(0, 0, 800, 600)

        self.show()
