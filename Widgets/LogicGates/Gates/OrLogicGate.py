from Widgets.LogicGates.Gates.LogicGate import LogicGate
from Widgets.LogicGates.Gates.Terminal import Terminal
from Widgets.LogicGates.GatesDesign.OR import GATE as OR


class OrLogicGate(LogicGate):
    def __init__(self, x, y, parent, scale, painterFactory):
        WIDTH = 250
        HEIGHT = 200
        super(OrLogicGate, self).__init__(x, y, WIDTH, HEIGHT, scale, parent, painterFactory)
        self.type = "OR"
        self.terminals = [
            Terminal("INPUT", 0, 40 - 5, self),
            Terminal("INPUT", 0, 160 - 5, self),
            Terminal("OUTPUT", 230, 100 - 5, self),
        ]

        self.show()

