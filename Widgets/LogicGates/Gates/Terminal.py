from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QPoint, QEvent
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QWidget


class Terminal(QWidget):
    def __init__(self, type, x, y, parent, multipleLinks=False):
        super(Terminal, self).__init__()
        self.__originalX = x
        self.__originalY = y
        self.type = None
        self.connection = None
        self.value = False
        self.setGeometry(int(x * parent.scaleX), int(y * parent.scaleY), 10, 10)
        self.setType(type)
        self.multipleLinks = multipleLinks

        self.setMouseTracking(True)

        self.setParent(parent)
        self.painter = QPainter(self)
        self.installEventFilter(self)
        self.pen = QtCore.Qt.red

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

    def setScale(self, x, y):
        self.scaleX, self.scaleY = x, y

        self.setGeometry(int(self.__originalX * self.scaleX), int(self.__originalY * self.scaleY), 10, 10)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        super(Terminal, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            self.parent().onTerminalPress(self)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        super(Terminal, self).mouseMoveEvent(event)

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.pen = QtCore.Qt.green
            self.repaint()
            return True
        elif event.type() == QEvent.Leave:
            self.pen = QtCore.Qt.red
            self.repaint()
        return False

    def relativePos(self):
        return self.pos() + self.parent().pos() + QPoint(5, 5)

    def connectTerminal(self, terminal):
        self.connectedTerminal = terminal

    def disconnectTerminal(self):
        self.connectedTerminal = None

    def getConnectedTerminal(self):
        return self.connectedTerminal
