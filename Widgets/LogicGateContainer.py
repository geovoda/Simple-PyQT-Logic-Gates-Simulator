from PyQt5.QtCore import QEvent, QRegularExpression
from PyQt5.QtGui import QPainter, QPen, QIntValidator, QFont, QRegularExpressionValidator
from PyQt5.QtWidgets import QWidget, QLayout, QPushButton, QLineEdit
from PyQt5 import QtGui
from PyQt5 import QtCore

from Widgets.LogicGates.AndLogicGate import AndLogicGate
from Widgets.LogicGates.InputStream import InputStream


class LogicGateContainer(QWidget):
    def __init__(self, parent=None):
        super(LogicGateContainer, self).__init__(parent)

        self.logicGates = []
        self.__linkingTerminal = None
        self.__mousePos = None

        self.setMouseTracking(True)

        self.painter = QPainter(self)

        self.initWindow()

        self.inputStream = InputStream(10, 40, self)

    def initWindow(self):
        self.undoButton = QPushButton(self)
        self.undoButton.setText("Undo")  # text
        self.undoButton.setShortcut('Ctrl+Z')  # shortcut key
        self.undoButton.clicked.connect(self.undo)
        self.undoButton.setToolTip("Anuleaza ultima actiune ")  # Tool tip
        self.undoButton.move(10, 1)

        self.redoButton = QPushButton(self)
        self.redoButton.setText("Redo")  # text
        self.redoButton.setShortcut('Ctrl+Z')  # shortcut key
        self.redoButton.clicked.connect(self.redo)
        self.redoButton.setToolTip("Reface ultima actiune")  # Tool tip
        self.redoButton.move(110, 1)

        self.simulateButton = QPushButton(self)
        self.simulateButton.setText("Simulare")  # text
        self.simulateButton.clicked.connect(self.toggleSimulation)
        self.simulateButton.setToolTip("Simuleaza circuitul")  # Tool tip
        self.simulateButton.move(210, 1)

        self.show()

    def toggleSimulation(self):
        print("Incep simularea")

    def undo(self):
        print("Undo")

    def redo(self):
        print("Redo")

    def addGate(self, type):
        if type == "AND":
            self.logicGates.append(AndLogicGate(0, 0, self))
        elif type == "INPUT_STREAM":
            self.logicGates.append(InputStream(0, 0, self))

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.__linkingTerminal is not None:
            self.__mousePos = e.pos()
            self.update()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == QtCore.Qt.LeftButton and self.__linkingTerminal is not None:
            self.__linkingTerminal = None
            self.update()

    def onTerminalPress(self, terminal):
        if terminal.getConnectedTerminal() is not None:
            # print("Terminal deja conectat")
            terminal.getConnectedTerminal().disconnectTerminal()
            terminal.disconnectTerminal()
        elif self.__linkingTerminal is None:
            print("Conectez terminalul nou")
            self.__linkingTerminal = terminal
        else:
            if self.__linkingTerminal.parent() is terminal.parent():
                # TODO - mesaj in interfata
                print("E aceasi poarta")
            elif self.__linkingTerminal.type == terminal.type:
                # TODO - mesaj in interfata
                print("E acelasi tip")
            else:
                self.__linkingTerminal.connectTerminal(terminal)
                terminal.connectTerminal(self.__linkingTerminal)
                self.__linkingTerminal = None
                self.__mousePos = None

        self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen()
        pen.setColor(QtCore.Qt.red)
        pen.setWidth(5)
        self.painter.setPen(pen)

        if self.__linkingTerminal is not None and self.__mousePos is not None:
            self.painter.drawLine(self.__linkingTerminal.relativePos().x(), self.__linkingTerminal.relativePos().y(), self.__mousePos.x(), self.__mousePos.y())

        for gate in self.logicGates:
            gate.paintTerminalLinks(self.painter)

        self.painter.end()
