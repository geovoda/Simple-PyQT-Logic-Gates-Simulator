from PyQt5 import QtCore
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator, QFont, QPainter, QPen
from PyQt5.QtWidgets import QLineEdit
from Widgets.LogicGates.Gates.LogicGate import LogicGate
from Widgets.LogicGates.Gates.Terminal import Terminal


class OutputStream(LogicGate):
    def __init__(self, x, y, parent, scale, paintFactory):
        WIDTH = 300
        HEIGHT = 60
        super(OutputStream, self).__init__(x, y, WIDTH, HEIGHT, scale, parent, paintFactory)
        self.type = "OUTPUT"
        self.terminals = [
            Terminal("INPUT", 1, 20, self),
            #Terminal("OUTPUT", 280, 20, self)
        ]
        self.setStyleSheet("background-color: yellow;")
        self.e1 = QLineEdit()
        self.e1.setValidator(QRegularExpressionValidator(QRegularExpression("[0-1]+")))
        self.e1.setMaxLength(10)
        self.e1.setGeometry(15, 0, 0, 0)
        self.e1.setFixedWidth(int(240 * self.scaleX))
        self.e1.setFixedHeight(int(56 * self.scaleY))
        self.e1.setFont(QFont("Arial", int(24 * self.scaleX)))
        self.e1.setParent(self)

        self.show()

    def setScale(self, x, y):
        super(OutputStream, self).setScale(x, y)
        self.e1.setFixedWidth(int(240 * self.scaleX))
        self.e1.setFixedHeight(int(56 * self.scaleX))
        self.e1.setFont(QFont("Arial", int(24 * self.scaleX)))
        self.e1.setDisabled(True)

    def paintGate(self):
        self.painter.drawLine(0, 30, 300, 30)

    def processOutput(self):
        text = ""
        for i in range(0, 10):
            text += str(self.terminals[0].getConnectedTerminal().getOutput(i))

        self.e1.setText(text)
