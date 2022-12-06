from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QLabel


class GateIcon(QLabel):
    def __init__(self, type, paintFactory):
        super().__init__()
        self.type = type

        self.paintFactory = paintFactory
        self.painter = QPainter(self)
        self.setFixedWidth(25)
        self.setFixedHeight(20)


    def paintEvent(self, event):
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.scale(0.1, 0.1)

        pen = QPen()
        pen.setColor(QtCore.Qt.white)
        pen.setWidth(15)
        self.painter.setPen(pen)

        self.paintFactory.paintGate(self.type, self.painter)

        self.painter.end()
