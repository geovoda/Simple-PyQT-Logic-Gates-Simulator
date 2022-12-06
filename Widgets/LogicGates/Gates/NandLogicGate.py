from Widgets.LogicGates.Gates.LogicGate import LogicGate
from Widgets.LogicGates.Gates.Terminal import Terminal
from Widgets.LogicGates.GatesDesign.NAND import GATE as NAND


class NandLogicGate(LogicGate):
    def __init__(self, x, y, parent, scale, painterFactory):
        WIDTH = 250
        HEIGHT = 200
        super(NandLogicGate, self).__init__(x, y, WIDTH, HEIGHT, scale, parent, painterFactory)
        self.type = "NAND"
        self.terminals = [
            Terminal("INPUT", 0, 40 - 5, self),
            Terminal("INPUT", 0, 160 - 5, self),
            Terminal("OUTPUT", 230, 100 - 5, self),
        ]

        self.show()
