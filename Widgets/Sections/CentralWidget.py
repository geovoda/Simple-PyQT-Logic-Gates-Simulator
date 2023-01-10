from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout

from Widgets.Sections.LogicGateContainer import LogicGateContainer
from Widgets.Sections.LogicGateMenu import LogicGateMenu
from Widgets.Sections.TopBar import TopBar


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.logicGateMenu = LogicGateMenu(self)
        self.logicGateContainer = LogicGateContainer(parent=self)
        self.topBar = TopBar(self)

        scrollableArea = QScrollArea()
        scrollableArea.setWidget(self.logicGateMenu)
        scrollableArea.setWidgetResizable(True)
        scrollableArea.setFixedWidth(84)
        scrollableArea.setStyleSheet("QScrollArea{border: none; border-right: 2px solid #c9d8ff;}")

        hbox = QHBoxLayout()
        hbox.addWidget(scrollableArea)
        hbox.addWidget(self.logicGateContainer, 1)
        hbox.setContentsMargins(0, 0, 0, 0)

        vbox = QVBoxLayout()
        vbox.addWidget(self.topBar)
        vbox.addLayout(hbox)
        vbox.setContentsMargins(0, 0, 0, 0)

        self.setLayout(vbox)