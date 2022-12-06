from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5 import QtCore
import math


class GateButton(QWidget):
    def __init__(self, type, parent):
        super().__init__()
        self.type = type
        self.setGeometry(0, 0, 300, 300)
        self.setParent(parent)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        # super(LogicGate, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.LeftButton:


    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        super().mouseMoveEvent(event)
        if event.buttons() == QtCore.Qt.LeftButton and self.__mousePressPosition is not None:
            self.move(self.mapToParent(event.pos() - self.__mousePressPosition))
            self.parent().repaint()

    def paintEvent(self, event):
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.scale(self.scaleX, self.scaleY)

        pen = QPen()
        pen.setColor(QtCore.Qt.black)
        pen.setWidth(5)


        self.painter.end()
