from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5 import QtCore
import math

class LogicGate(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.mousePressPosition = None

        self.scaleX = 1
        self.scaleY = 1

        self.painter = QPainter(self)
        self.terminals = []
        self.setMouseTracking(True)
        self.setParent(parent)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            self.mousePressPosition = event.pos()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        super().mouseMoveEvent(event)
        if event.buttons() == QtCore.Qt.LeftButton and self.mousePressPosition is not None:
            newPos = self.mapToParent(event.pos() - self.mousePressPosition)

            if newPos.x() < 0:
                newPos.setX(0)

            if newPos.y() < 0:
                newPos.setY(0)
            self.move(newPos)
            self.parent().update()

    def setScale(self, x, y):
        self.scaleX, self.scaleY = x, y

    def paintGate(self):
        pass

    def paintTerminalLinks(self, painter: QPainter):
        # Lista in care punem terminalele intre care liniile au fost deja desenate
        tmp = []
        for terminal in self.terminals:
            if terminal not in tmp and terminal.getConnectedTerminal() is not None:
                pos1 = terminal.relativePos()
                pos2 = terminal.getConnectedTerminal().relativePos()

                painter.drawLine(pos1.x(), pos1.y(), pos2.x(), pos2.y())

                tmp.append(terminal)
                tmp.append(terminal.getConnectedTerminal())

    def onTerminalPress(self, terminal):
        self.parent().onTerminalPress(terminal)

    def paintEvent(self, event):
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.scale(self.scaleX, self.scaleY)

        pen = QPen()
        pen.setColor(QtCore.Qt.black)
        pen.setWidth(5)
        self.painter.setPen(pen)

        self.paintGate()

        self.painter.end()
