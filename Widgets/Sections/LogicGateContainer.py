from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5 import QtGui
from PyQt5 import QtCore

from Widgets.LogicGates.Factories.LogicGateFactory import LogicGateFactory
# from Widgets.LogicGates.Gates.AndLogicGate import AndLogicGate
# from Widgets.LogicGates.Gates.InputStream import InputStream
# from Widgets.LogicGates.Gates.NandLogicGate import NandLogicGate
# from Widgets.LogicGates.Gates.NorLogicGate import NorLogicGate
# from Widgets.LogicGates.Gates.OrLogicGate import OrLogicGate
# from Widgets.LogicGates.Gates.OutputStream import OutputStream
# from Widgets.LogicGates.Gates.XnorLogicGate import XnorLogicGate
# from Widgets.LogicGates.Gates.XorLogicGate import XorLogicGate


class LogicGateContainer(QWidget):
    def __init__(self, parent=None):
        super(LogicGateContainer, self).__init__(parent)

        self.logicGates = []
        self.__linkingTerminal = None
        self.__mousePos = None

        self.scaleX = 0.5
        self.scaleY = 0.5

        self.setMouseTracking(True)

        self.painter = QPainter(self)

        self.initWindow()

        self.logicGatesFactory = LogicGateFactory()

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

        self.zoomInButton = QPushButton(self)
        self.zoomInButton.setText("Zoom in")
        self.zoomInButton.clicked.connect(self.zoomIn)
        self.zoomInButton.move(310, 1)

        self.zoomOutButton = QPushButton(self)
        self.zoomOutButton.setText("Zoom out")  # text
        self.zoomOutButton.clicked.connect(self.zoomOut)
        self.zoomOutButton.move(410, 1)

        self.show()

    def zoomIn(self):
        print("Zoom In")

        self.scaleX = self.scaleX + 0.1
        self.scaleY = self.scaleY + 0.1

        for gate in self.logicGates:
            gate.setScale(self.scaleX, self.scaleY)

        self.repaint()

    def zoomOut(self):
        print("Zoom In")

        self.scaleX = self.scaleX - 0.1
        self.scaleY = self.scaleY - 0.1

        for gate in self.logicGates:
            gate.setScale(self.scaleX, self.scaleY)

        self.repaint()

    def toggleSimulation(self):
        outputList = []

        # Verificam daca au fost conectate toate bornele
        for gate in self.logicGates:
            for terminal in gate.terminals:
                if terminal.getConnectedTerminal() is None:
                    print("Nu toate bornele sunt conectate")
                    return

            if gate.type == "OUTPUT":
                outputList.append(gate)

            if gate.type == "INPUT":
                gate.prepareGate()

        for gate in outputList:
            gate.processOutput()











    def undo(self):
        print("Undo")

    def redo(self):
        print("Redo")

    def addGate(self, type):
        gate = self.logicGatesFactory.create(type, 0, 30, (self.scaleX, self.scaleY), self)
        self.logicGates.append(gate)
        # if type == "AND":
        #     self.logicGates.append(AndLogicGate(0, 30, self, (self.scaleX, self.scaleY)))
        # elif type == "OR":
        #     self.logicGates.append(OrLogicGate(0, 30, self, (self.scaleX, self.scaleY)))
        # elif type == "XOR":
        #     self.logicGates.append(XorLogicGate(0, 30, self, (self.scaleX, self.scaleY)))
        # elif type == "NAND":
        #     self.logicGates.append(NandLogicGate(0, 30, self, (self.scaleX, self.scaleY)))
        # elif type == "NOR":
        #     self.logicGates.append(NorLogicGate(0, 30, self, (self.scaleX, self.scaleY)))
        # elif type == "XNOR":
        #     self.logicGates.append(XnorLogicGate(0, 30, self, (self.scaleX, self.scaleY)))
        # elif type == "INPUT_STREAM":
        #     self.logicGates.append(InputStream(0, 30, self, (self.scaleX, self.scaleY)))
        # elif type == "OUTPUT_STREAM":
        #     self.logicGates.append(OutputStream(0, 30, self, (self.scaleX, self.scaleY)))



    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.__linkingTerminal is not None:
            self.__mousePos = e.pos()
            self.repaint()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == QtCore.Qt.LeftButton and self.__linkingTerminal is not None:
            self.__linkingTerminal = None
            self.__mousePos = None
            self.repaint()

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

        self.repaint()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen()
        pen.setColor(QtCore.Qt.red)
        pen.setWidth(5)
        self.painter.setPen(pen)

        if self.__linkingTerminal is not None and self.__mousePos is not None:
            self.painter.drawLine(self.__linkingTerminal.relativePos().x(), self.__linkingTerminal.relativePos().y(),
                                  self.__mousePos.x(), self.__mousePos.y())

        for gate in self.logicGates:
            gate.paintTerminalLinks(self.painter)

        self.painter.end()
