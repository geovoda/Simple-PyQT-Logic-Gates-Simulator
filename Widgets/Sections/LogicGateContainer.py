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

        self.save1 = None

        self.save2 = None

        self.save3 = None

        self.save4 = None

        self.save5 = None

        self.pos = 0

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

            if gate.type == "OUTPUT_STREAM":
                outputList.append(gate)

            if gate.type == "INPUT_STREAM":
                gate.prepareGate()

        for gate in outputList:
            gate.processOutput()

    def undo(self):
        if self.pos == 5:
            self.loadProjectContent(self.save4)
            self.pos = 4
        elif self.pos == 4:
            self.loadProjectContent(self.save3)
            self.pos = 3
        elif self.pos == 3:
            self.loadProjectContent(self.save2)
            self.pos = 2
        elif self.pos == 2:
            self.loadProjectContent(self.save1)
            self.pos = 1
        print(self.pos)

    def redo(self):
        if self.pos == 4 and self.save5 is not None:
            self.loadProjectContent(self.save5)
            self.pos = 5
        elif self.pos == 3 and self.save4 is not None:
            self.loadProjectContent(self.save4)
            self.pos = 4
        elif self.pos == 2 and self.save3 is not None:
            self.loadProjectContent(self.save3)
            self.pos = 3
        elif self.pos == 1 and self.save2 is not None:
            self.loadProjectContent(self.save2)
            self.pos = 2
        print(self.pos)

    def addGate(self, type, x=0, y=30):
        gate = self.logicGatesFactory.create(type, x, y, self.scale, self)
        self.logicGates.append(gate)
        self.SaveUndo()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.__linkingTerminal is not None:
            self.__mousePos = e.pos()
            self.repaint()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == QtCore.Qt.LeftButton and self.__linkingTerminal is not None:
            self.__linkingTerminal = None
            self.__mousePos = None
            self.repaint()

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.SaveUndo()

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
                    connectedTerminal = terminal.getConnectedTerminal()

                terminals.append({
                    "parent-uuid": terminal.parent().uuid,
                    "parent-index": index,
                    "pair-parent-uuid": connectedTerminal.parent().uuid,
                    "pair-parent-index": connectedTerminal.getIndex(),
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

    def generateProjectContentUndo(self):
        terminals = []
        gates = []

        for gate in self.logicGates:
            for index, terminal in enumerate(gate.terminals):
                connectedTerminalUUID = None

                if terminal.getConnectedTerminal() is not None:
                    connectedTerminal = terminal.getConnectedTerminal()

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
    def SaveUndo(self):
        if self.pos==0:
             self.save1= self.generateProjectContentUndo()
             self.pos = 1
             self.save2 = None
        elif self.pos==1:
             self.save2 = self.generateProjectContentUndo()
             self.pos = 2
             self.save3 = None
        elif self.pos==2:
             self.save4 = None
             self.save3 = self.generateProjectContentUndo()
             self.pos = 3
        elif self.pos==3:
             self.save5 = None
             self.save4 = self.generateProjectContentUndo()
             self.pos = 4
        elif self.pos == 4:
             self.save5 = None
             self.save5 = self.generateProjectContentUndo()
             self.pos = 5
        elif self.pos==5:
             self.save1 = self.save2
             self.save2 = self.save3
             self.save3 = self.save4
             self.save4 = self.save5
             self.save5 = self.generateProjectContentUndo()
        print(self.pos)

    def loadProjectContent(self, content):
        for gate in self.logicGates:
            gate.deleteLater()

        self.logicGates = []
        gates = {}

        for gate in content["gates"]:
            createdGate = self.logicGatesFactory.create(gate["type"], gate["x"], gate["y"], self.scale, self)
            gates[gate["uuid"]] = createdGate

        for terminal in content["terminals"]:
            if gates[terminal["parent-uuid"]].terminals[terminal["parent-index"]].getConnectedTerminal() is None:
                gates[terminal["parent-uuid"]].terminals[terminal["parent-index"]].connectTerminal(gates[terminal["pair-parent-uuid"]].terminals[terminal["pair-parent-index"]])

            if gates[terminal["pair-parent-uuid"]].terminals[terminal["pair-parent-index"]].getConnectedTerminal() is None:
                gates[terminal["pair-parent-uuid"]].terminals[terminal["pair-parent-index"]].connectTerminal(gates[terminal["parent-uuid"]].terminals[terminal["parent-index"]])

        for gateKey in gates:
            self.logicGates.append(gates[gateKey])

        self.repaint()

