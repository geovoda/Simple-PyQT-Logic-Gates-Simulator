from Widgets.LogicGates.Gates.LogicGate import LogicGate
from Widgets.LogicGates.Gates.Terminal import Terminal
from Widgets.LogicGates.GatesDesign.XNOR import GATE as XNOR


class XnorLogicGate(LogicGate):
    def __init__(self, x, y, parent, scale, painterFactory):
        WIDTH = 250
        HEIGHT = 200
        super(XnorLogicGate, self).__init__(x, y, WIDTH, HEIGHT, scale, parent, painterFactory)
        self.type = "XNOR"
        self.terminals = [
            Terminal("INPUT", 0, 40 - 5, self),
            Terminal("INPUT", 0, 160 - 5, self),
            Terminal("OUTPUT", 230, 100 - 5, self),
        ]

        self.show()

    def makeOperation(self, item1, item2):
        return not(item1 ^ item2)
