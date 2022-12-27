from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QPushButton, QSlider, QHBoxLayout, QLabel
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

        self.scale = 0.5

        self.setMouseTracking(True)

        self.painter = QPainter(self)

        self.initWindow()

        self.logicGatesFactory = LogicGateFactory()

    def initWindow(self):
        layout = QHBoxLayout()

        simulateButton = QPushButton(self)
        simulateButton.setText("Simulare")  # text
        simulateButton.clicked.connect(self.toggleSimulation)
        simulateButton.setToolTip("Simuleaza circuitul")  # Tool tip
        simulateButton.setStyleSheet("QPushButton{border: none; background-color: blue; padding: 5px 20px; color: white; border-radius: 5px;} QPushButton:hover{background-color: red;}")
        simulateButton.move(210, 1)
        layout.addWidget(simulateButton)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(90)
        self.slider.setValue(50)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(2)
        self.slider.move(410, 1)
        self.slider.valueChanged.connect(self.processZoom)
        layout.addWidget(self.slider)
        layout.setAlignment(Qt.AlignTop)

        self.setLayout(layout)

        self.show()

    def processZoom(self):
        self.scale = self.slider.value() / 100

        for gate in self.logicGates:
            gate.setScale(self.scale)

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

    def addGate(self, type, x=0, y=30):
        gate = self.logicGatesFactory.create(type, x, y, self.scale, self)
        self.logicGates.append(gate)

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
            # terminal.getConnectedTerminal().disconnectTerminal()
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

    def removeGate(self, gate):
        if gate in self.logicGates:
            self.logicGates.remove(gate)

    def removeAllGates(self):
        for gate in self.logicGates:
            gate.deleteLater()

        self.logicGates = []
        self.repaint()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen()
        pen.setColor(QtCore.Qt.black)
        pen.setWidth(3)
        self.painter.setPen(pen)

        if self.__linkingTerminal is not None and self.__mousePos is not None:
            self.painter.drawLine(self.__linkingTerminal.relativePos().x(), self.__linkingTerminal.relativePos().y(),
                                  self.__mousePos.x(), self.__mousePos.y())

        for gate in self.logicGates:
            gate.paintTerminalLinks(self.painter)

        self.painter.end()

    def generateProjectContent(self):
        terminals = []
        gates = []

        for gate in self.logicGates:
            for index, terminal in enumerate(gate.terminals):
                connectedTerminalUUID = None

                if terminal.getConnectedTerminal() is not None:
                    connectedTerminalUUID = terminal.getConnectedTerminal().uuid

                terminals.append({
                    "index": index,
                    "uuid": terminal.uuid,
                    "pair-uuid": connectedTerminalUUID,
                    "parent-uuid": terminal.parent().uuid,
                })

            gates.append({
                "uuid": gate.uuid,
                "type": gate.type,
                "x": gate.x(),
                "y": gate.y(),
            })

        return {
            "gates": gates,
            "terminals": terminals
        }

    def loadProjectContent(self, content):
        gates = {}
        terminals = {}

        for gate in content["gates"]:
            createdGate = self.logicGatesFactory.create(type, gate["x"], gate["y"], self.scale, self)
            gates[gate["uuid"]] = createdGate

        for terminal in content["terminals"]:
            pass