from PyQt5 import QtCore
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator, QFont, QPainter, QPen
from PyQt5.QtWidgets import QLineEdit

from Widgets.LogicGates.LogicGate import LogicGate
from Widgets.LogicGates.Terminal import Terminal


class InputStream(LogicGate):
    def __init__(self, x, y, parent):
        super(InputStream, self).__init__(parent)
        self.setGeometry(x, y, int(300 * self.scaleX), int(60 * self.scaleY))

        self.terminals = [
            Terminal("OUTPUT", 280, 20, self),
        ]
        self.setStyleSheet("background-color: yellow;")

        self.e1 = QLineEdit()
        self.e1.setValidator(QRegularExpressionValidator(QRegularExpression("[0-1]+")))
        self.e1.setMaxLength(10)
        self.e1.setFixedWidth(120)
        self.e1.setFont(QFont("Arial", 12))
        self.e1.setParent(self)

        self.show()

    def paintGate(self):
        self.painter.drawLine(0, 30, 300, 30)
