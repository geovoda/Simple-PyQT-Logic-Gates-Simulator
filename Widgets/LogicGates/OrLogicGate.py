from Widgets.LogicGates.LogicGate import LogicGate
from Widgets.LogicGates.LogicGateFactoryOld import LogicGateFactoryOld
from Widgets.LogicGates.Terminal import Terminal


class OrLogicGate(LogicGate):
    def __init__(self, x, y, parent, scale):
        WIDTH = 250
        HEIGHT = 200
        super(OrLogicGate, self).__init__(x, y, WIDTH, HEIGHT, scale, parent)

        self.terminals = [
            Terminal("INPUT", 0, 40 - 5, self),
            Terminal("INPUT", 0, 160 - 5, self),
            Terminal("OUTPUT", 230, 100 - 5, self),
        ]

        self.show()

    def paintGate(self):
        LogicGateFactoryOld().paint(self.painter)
