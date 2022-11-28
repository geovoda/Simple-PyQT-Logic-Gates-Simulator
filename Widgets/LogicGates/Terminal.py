from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QPoint, QEvent
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QWidget


class Terminal(QWidget):
    def __init__(self, type, x, y, parent):
        super(Terminal, self).__init__()
        self.type = None
        self.connection = None
        self.value = False
        self.setGeometry(x, y, 10, 10)
        self.setType(type)

        #self.setMouseTracking(True)

        self.setParent(parent)
        self.painter = QPainter(self)
        self.installEventFilter(self)
        self.pen = QtCore.Qt.red

        self.connectedTerminal: Terminal = None

    def setType(self, type):
        if type != "INPUT" and type != "OUTPUT":
            self.type = "INPUT"
        else:
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

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            self.parent().onTerminalPress(self)

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.pen = QtCore.Qt.green
            self.update()
            return True
        elif event.type() == QEvent.Leave:
            self.pen = QtCore.Qt.red
            self.update()
        return False

    def relativePos(self):
        return self.pos() + self.parent().pos() + QPoint(5, 5)

    def connectTerminal(self, terminal):
        self.connectedTerminal = terminal

    def getConnectedTerminal(self):
        return self.connectedTerminal
