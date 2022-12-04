from Widgets.LogicGates.LogicGate import LogicGate
from Widgets.LogicGates.LogicGateFactory import LogicGateFactory
from Widgets.LogicGates.Terminal import Terminal


class AndLogicGate(LogicGate):
    def __init__(self, x, y, parent, scale):
        WIDTH = 250
        HEIGHT = 200
        super(AndLogicGate, self).__init__(x, y, WIDTH, HEIGHT, scale, parent)

        self.terminals = [
            Terminal("INPUT", 0, 40 - 5, self),
            Terminal("INPUT", 0, 160 - 5, self),
            Terminal("OUTPUT", 230, 100 - 5, self),
        ]

        self.show()

    def paintGate(self):
        LogicGateFactory().paint(self.painter)
