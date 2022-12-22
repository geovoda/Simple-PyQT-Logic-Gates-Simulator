import uuid as uuid_lib

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QPoint, QEvent
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QWidget


class Terminal(QWidget):
    def __init__(self, type, x, y, parent, multipleLinks=False, uuid=None):
        super(Terminal, self).__init__()
        if uuid is None:
            self.uuid = str(uuid_lib.uuid1())
        else:
            self.uuid = uuid
        self.__originalX = x
        self.__originalY = y
        self.type = None
        self.connection = None
        self.value = False
        self.setGeometry(int(x * parent.scale), int(y * parent.scale), 10, 10)
        self.setType(type)
        self.multipleLinks = multipleLinks

        self.setMouseTracking(True)

        self.setParent(parent)
        self.painter = QPainter(self)
        self.installEventFilter(self)
        self.pen = QColor(41, 98, 255)

        self.connectedTerminal = None

    def setType(self, type):
        if type == "INPUT" or type == "OUTPUT":
            self.type = type

    def getType(self):
        return self.type

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)

        # pen = QPen()
        # pen.setColor(QtCore.Qt.black)
        # pen.setWidth(3)
        # self.painter.setPen(pen)

        self.painter.setBrush(self.pen)
        self.painter.drawEllipse(0, 0, 10, 10)

        self.painter.end()

    def setScale(self, scale):
        self.scale = scale
        print(scale)

        self.setGeometry(int(self.__originalX * self.scale), int(self.__originalY * self.scale), 10, 10)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        super(Terminal, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            self.parent().onTerminalPress(self)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        super(Terminal, self).mouseMoveEvent(event)

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            if self.connectedTerminal is None:
                self.pen = QtCore.Qt.green
            else:
                self.pen = QtCore.Qt.red
            self.repaint()
            return True
        elif event.type() == QEvent.Leave:
            self.pen = QColor(41, 98, 255)
            self.repaint()
        return False

    def relativePos(self):
        return self.pos() + self.parent().pos() + QPoint(5, 5)

    def connectTerminal(self, terminal):
        self.connectedTerminal = terminal

    def disconnectTerminal(self, callPair=True):
        if self.connectedTerminal is not None:
            if callPair == True:
                self.connectedTerminal.disconnectTerminal(callPair=False)
            self.connectedTerminal = None

    def getConnectedTerminal(self):
        return self.connectedTerminal

    def getOutput(self, index):
        return self.parent().getOutput(index)