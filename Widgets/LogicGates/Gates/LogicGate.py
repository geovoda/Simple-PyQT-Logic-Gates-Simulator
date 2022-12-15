from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5 import QtCore
import math


class LogicGate(QWidget):
    def __init__(self, x, y, width, height, scale, parent, painterFactory):
        super().__init__()
        self.type = None
        self.__originalWidth = width
        self.__originalHeight = height

        self.__mousePressPosition = None

        self.scaleX, self.scaleY = scale
        self.setGeometry(x, y, int(width * self.scaleX), int(height * self.scaleY))
        self.painter = QPainter(self)
        self.terminals = []
        self.setMouseTracking(True)
        self.setParent(parent)

        self.input1 = 0
        self.input2 = 0
        self.output = 0

        self.painterFactory = painterFactory

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        # super(LogicGate, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            self.__mousePressPosition = event.pos()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        super().mouseMoveEvent(event)
        if event.buttons() == QtCore.Qt.LeftButton and self.__mousePressPosition is not None:
            self.move(self.mapToParent(event.pos() - self.__mousePressPosition))
            self.parent().repaint()

    def setScale(self, x, y):
        self.scaleX, self.scaleY = x, y

        self.setGeometry(self.x(), self.y(), int(self.__originalWidth * self.scaleX),
                         int(self.__originalHeight * self.scaleY))

        for terminal in self.terminals:
            terminal.setScale(x, y)

    def paintGate(self):
        self.painterFactory.paintGate(self.type, self.painter)

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
        pen.setColor(QColor(41, 98, 255))
        pen.setWidth(5)
        self.painter.setPen(pen)

        self.paintGate()

        self.painter.end()

    # def getInput(self):
    #     for terminal in self.terminals:
    #         if terminal.type == "INPUT":

    def makeOperation(self, item1, item2):
        pass

    def getOutput(self, index):
        inputResults = []
        for terminal in self.terminals:
            if terminal.type == "INPUT":
                inputResults.append(terminal.getConnectedTerminal().getOutput(index))

        result = inputResults[0]
        for item in inputResults:
            result = self.makeOperation(result, item)

        return result
